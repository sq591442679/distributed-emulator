/*
 * OSPF calculation.
 * Copyright (C) 1999 Kunihiro Ishiguro
 *
 * This file is part of GNU Zebra.
 *
 * GNU Zebra is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation; either version 2, or (at your option) any
 * later version.
 *
 * GNU Zebra is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program; see the file COPYING; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
 */

#ifndef _QUAGGA_OSPF_SPF_H
#define _QUAGGA_OSPF_SPF_H

#include "typesafe.h"

/* values for vertex->type */
#define OSPF_VERTEX_ROUTER  1  /* for a Router-LSA */
#define OSPF_VERTEX_NETWORK 2  /* for a Network-LSA */

/* values for vertex->flags */
#define OSPF_VERTEX_PROCESSED      0x01

/* The "root" is the node running the SPF calculation */

PREDECL_SKIPLIST_NONUNIQ(vertex_pqueue);
/* A router or network in an area */
struct vertex {
	struct vertex_pqueue_item pqi;
	uint8_t flags;
	uint8_t type;		/* copied from LSA header */
	struct in_addr id;      /* copied from LSA header */
	struct ospf_lsa *lsa_p;
	struct lsa_header *lsa; /* Router or Network LSA */
	uint32_t distance;      /* from root to this vertex */
	struct list *parents;   /* list of parents in SPF tree */
	struct list *children;  /* list of children in SPF tree*/
};

struct vertex_nexthop {
	struct in_addr router;     /* router address to send to */
	int lsa_pos; /* LSA position for resolving the interface */
};

struct vertex_parent {
	struct vertex_nexthop *nexthop; /* nexthop taken on the root node */
	struct vertex_nexthop *local_nexthop; /* local nexthop of the parent */
	struct vertex *parent;		      /* parent vertex */
	int backlink; /* index back to parent for router-lsa's */
};

/**
 * @author sqsq
 * @brief object used to maintain bfs search path
 */
PREDECL_HASH(node_dict);
struct node_item {
	struct ospf_lsa *lsa;
	struct node_dict_item hash_item;
};
extern struct node_item *node_item_new(void);
extern struct node_item *node_item_init(struct ospf_lsa *lsa);
extern void node_item_free(struct node_item *item);
extern int node_item_compare_func(const struct node_item *a, 
											const struct node_item *b);
extern uint32_t node_item_hash_func(const struct node_item *a);
DECLARE_HASH(node_dict, struct node_item, hash_item, 
				node_item_compare_func, node_item_hash_func);

/**
 * @author sqsq
 */
PREDECL_HASH(path_dict);
struct path_item {
	struct in_addr nexthop;
	struct ospf_path *path;
	struct path_dict_item path_dict_field;
};
extern int path_item_compare_func(const struct path_item *a, const struct path_item *b);
extern uint32_t path_item_hash_func(const struct path_item *a);
extern struct path_item *path_item_new(void);
extern struct path_item *path_item_init(struct in_addr nexthop);
extern void path_item_free(struct path_item *item);
DECLARE_HASH(path_dict, struct path_item, path_dict_field, path_item_compare_func, path_item_hash_func);


/**
 * @author sqsq
 */
PREDECL_LIST(search_item_queue);				// Z1 = search_item_queue
PREDECL_HASH(search_item_dict);
/**
 * object used in bfs search
 */
struct search_item {
	struct node_item *current_node;
	uint32_t hop_cnt;									// hop cnt from root to current router
	uint32_t cost;										// min cost from root to current router
	struct node_dict_head parents_dict_head;			// dict of node_item
	struct path_dict_head nexthop_dict_head;			// dict of path_item
	struct search_item_queue_item queue_item;
	struct search_item_dict_item hash_item;
};
DECLARE_LIST(search_item_queue, struct search_item, queue_item);
extern struct search_item *search_item_new(void);
extern struct search_item *search_item_init(struct ospf_lsa *lsa, uint32_t hop_cnt, uint32_t cost);
extern void search_item_free(struct search_item *item);
extern void search_item_add_parent(struct search_item *item, struct search_item *parent);
extern int search_item_compare_func(const struct search_item *a, const struct search_item *b);
extern uint32_t search_item_hash_func(const struct search_item *a);
DECLARE_HASH(search_item_dict, struct search_item, hash_item, search_item_compare_func, search_item_hash_func);

extern void search_item_add_nexthop(struct ospf_area *area, struct search_item *item, struct search_item *neighbor_item, struct search_item *root_item, struct router_lsa_link *l);



/* What triggered the SPF ? */
typedef enum {
	SPF_FLAG_ROUTER_LSA_INSTALL = 1,
	SPF_FLAG_NETWORK_LSA_INSTALL,
	SPF_FLAG_SUMMARY_LSA_INSTALL,
	SPF_FLAG_ASBR_SUMMARY_LSA_INSTALL,
	SPF_FLAG_MAXAGE,
	SPF_FLAG_ABR_STATUS_CHANGE,
	SPF_FLAG_ASBR_STATUS_CHANGE,
	SPF_FLAG_CONFIG_CHANGE,
	SPF_FLAG_GR_FINISH,
} ospf_spf_reason_t;

/**
 * @author sqsq
 * @brief 
 * There can be multiple directions from satellite A to satellite B. 
 * @example
 * satellite (0, 4) to (1, 5) is both ORBIT_ID_INC_DIRECTION and INNER_ORBIT_ID_INC_DIRECTION
 */
typedef enum {
	ORBIT_ID_INC_DIRECTION = 1,
	ORBIT_ID_DEC_DIRECTION = (1 << 1),
	INNER_ORBIT_ID_INC_DIRECTION = (1 << 2),
	INNER_ORBIT_ID_DEC_DIRECTION = (1 << 3),
} ospf_spf_direction;

extern void ospf_spf_calculate_schedule(struct ospf *, ospf_spf_reason_t);
extern void ospf_spf_calculate(struct ospf_area *area,
			       struct ospf_lsa *root_lsa,
			       struct route_table *new_table,
			       struct route_table *all_rtrs,
			       struct route_table *new_rtrs, bool is_dry_run,
			       bool is_root_node);
extern void ospf_spf_calculate_area(struct ospf *ospf, struct ospf_area *area,
				    struct route_table *new_table,
				    struct route_table *all_rtrs,
				    struct route_table *new_rtrs);
extern void ospf_spf_calculate_areas(struct ospf *ospf,
				     struct route_table *new_table,
				     struct route_table *all_rtrs,
				     struct route_table *new_rtrs);
extern void ospf_rtrs_free(struct route_table *);
extern void ospf_spf_cleanup(struct vertex *spf, struct list *vertex_list);
extern void ospf_spf_copy(struct vertex *vertex, struct list *vertex_list);
extern void ospf_spf_remove_resource(struct vertex *vertex,
				     struct list *vertex_list,
				     struct protected_resource *resource);
extern struct vertex *ospf_spf_vertex_find(struct in_addr id,
					   struct list *vertex_list);
extern struct vertex *ospf_spf_vertex_by_nexthop(struct vertex *root,
						 struct in_addr *nexthop);
extern struct vertex_parent *ospf_spf_vertex_parent_find(struct in_addr id,
							 struct vertex *vertex);
extern int vertex_parent_cmp(void *aa, void *bb);

extern void ospf_spf_print(struct vty *vty, struct vertex *v, int i);
extern void ospf_restart_spf(struct ospf *ospf);
/* void ospf_spf_calculate_timer_add (); */

/** @sqsq */
extern void ospf_spf_calculate_rule(struct ospf_area *area, struct ospf_lsa *root_lsa,
			struct route_table *new_table,
			struct route_table *all_rtrs,
			struct route_table *new_rtrs, bool is_dry_run,
			bool is_root_node);
#endif /* _QUAGGA_OSPF_SPF_H */

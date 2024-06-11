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

/**
 * sqsq
 */
#include "ospfd/ospf_route.h"
#include "monotime.h"

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

/**
 * @author sqsq
 */
PREDECL_HASH(bfs_vertex_dict);
PREDECL_LIST(bfs_vertex_list);
struct bfs_vertex {
	uint8_t flags;			/** flags used in bfs_spf_process_stubs */
	struct in_addr id;      /* copied from LSA header */
	struct ospf_lsa *lsa_p;
	struct lsa_header *lsa; /* Router or Network LSA */
	uint32_t distance;      /* from root to this vertex */
	
	uint32_t hop;			/** hop cnt from root */
	struct bfs_vertex_dict_item hash_item;
	struct bfs_vertex_list_item list_item;

	struct list *parents;   /* list of parents in SPF tree (struct bfs_vertex_parent) */
	struct list *children;	/** list of children (struct bfs_vertex) */
};
struct bfs_vertex_nexthop {
	struct in_addr nexthop;     /* ip address to send to */
	struct ospf_interface *oi;
	// uint32_t cost;
};
struct bfs_vertex_parent {
	struct bfs_vertex_nexthop *nexthop;
	struct bfs_vertex *parent;		      /* parent vertex */
};

/**
 * sqsq
 */
extern void dump_excution_time(const char *func_name, struct timespec *start);

/**
 * @author sqsq
 */
extern struct bfs_vertex_parent *bfs_add_parent(struct bfs_vertex *v, struct bfs_vertex *w, struct bfs_vertex_nexthop *newhop);
extern int bfs_nexthop_calculation(struct ospf_area *area, struct bfs_vertex *v,  struct bfs_vertex *w, struct router_lsa_link *l, uint32_t distance);
extern void bfs_spf_next(struct bfs_vertex *v, struct ospf_area *area, struct bfs_vertex_list_head *bfs_queue);
extern void bfs_set_nexthops(struct ospf_area *area, struct ospf_route *or, int lsa_pos, struct bfs_vertex *v);
extern void bfs_spf_process_stubs(struct ospf_area *area, struct bfs_vertex *v, struct route_table *new_table);
extern void bfs_spf_calculate(struct ospf_area *area, struct ospf_lsa *root_lsa, struct route_table *new_table, struct list *bfs_vertex_list);

/**
 * sqsq
 */
extern struct bfs_vertex_nexthop *bfs_vertex_nexthop_new(void);
extern void bfs_vertex_nexthop_free(struct bfs_vertex_nexthop *nh);
extern int bfs_vertex_nexthop_cmp(void *aa, void *bb);

/**
 * sqsq
 */
extern struct bfs_vertex_parent *bfs_vertex_parent_new(struct bfs_vertex *v, struct bfs_vertex_nexthop *nh);
extern void bfs_vertex_parent_free(struct bfs_vertex_parent *a);
extern int bfs_vertex_parent_cmp(void *aa, void *bb);

/**
 * sqsq
 */
extern int bfs_vertex_compare_func(const struct bfs_vertex *a, const struct bfs_vertex *b);
extern uint32_t bfs_vertex_hash_func(const struct bfs_vertex *a);
extern struct bfs_vertex *bfs_vertex_new(struct ospf_area *area, struct ospf_lsa *lsa);
extern void bfs_vertex_free(void *data);
extern void bfs_vertex_dump(const struct bfs_vertex *a);
extern void bfs_vertex_add_parents(struct bfs_vertex *v);
DECLARE_LIST(bfs_vertex_list, struct bfs_vertex, list_item);
DECLARE_HASH(bfs_vertex_dict, struct bfs_vertex, hash_item, bfs_vertex_compare_func, bfs_vertex_hash_func);

#endif /* _QUAGGA_OSPF_SPF_H */

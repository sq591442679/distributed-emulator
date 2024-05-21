/*
 * Library-specific error messages.
 * Copyright (C) 2018  Cumulus Networks, Inc.
 *                     Donald Sharp
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the Free
 * Software Foundation; either version 2 of the License, or (at your option)
 * any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
 * more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program; see the file COPYING; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
 */

#ifndef __LIB_ERRORS_H__
#define __LIB_ERRORS_H__

#include "lib/ferr.h"

#ifdef __cplusplus
extern "C" {
#endif

enum lib_log_refs {
	EC_LIB_PRIVILEGES = LIB_FERR_START,
	EC_LIB_VRF_START,
	EC_LIB_SOCKET,
	EC_LIB_ZAPI_MISSMATCH,
	EC_LIB_ZAPI_ENCODE,
	EC_LIB_ZAPI_SOCKET,
	EC_LIB_SYSTEM_CALL,
	EC_LIB_VTY,
	EC_LIB_INTERFACE,
	EC_LIB_NS,
	EC_LIB_DEVELOPMENT,
	EC_LIB_ZMQ,
	EC_LIB_UNAVAILABLE,
	EC_LIB_SNMP,
	EC_LIB_STREAM,
	EC_LIB_LINUX_NS,
	EC_LIB_SLOW_THREAD_CPU,
	EC_LIB_SLOW_THREAD_WALL,
	EC_LIB_STARVE_THREAD,
	EC_LIB_NO_THREAD,
	EC_LIB_TIMER_TOO_LONG,
	EC_LIB_RMAP_RECURSION_LIMIT,
	EC_LIB_BACKUP_CONFIG,
	EC_LIB_VRF_LENGTH,
	EC_LIB_YANG_MODULE_LOAD,
	EC_LIB_YANG_MODULE_LOADED_ALREADY,
	EC_LIB_YANG_DATA_CONVERT,
	EC_LIB_YANG_DATA_TRUNCATED,
	EC_LIB_YANG_UNKNOWN_DATA_PATH,
	EC_LIB_YANG_DNODE_NOT_FOUND,
	EC_LIB_YANG_TRANSLATOR_LOAD,
	EC_LIB_YANG_TRANSLATION_ERROR,
	EC_LIB_NB_DATABASE,
	EC_LIB_NB_CB_UNNEEDED,
	EC_LIB_NB_CB_MISSING,
	EC_LIB_NB_CB_INVALID_PRIO,
	EC_LIB_NB_CBS_VALIDATION,
	EC_LIB_NB_CB_CONFIG_VALIDATE,
	EC_LIB_NB_CB_CONFIG_PREPARE,
	EC_LIB_NB_CB_CONFIG_ABORT,
	EC_LIB_NB_CB_CONFIG_APPLY,
	EC_LIB_NB_CB_STATE,
	EC_LIB_NB_CB_RPC,
	EC_LIB_NB_CANDIDATE_INVALID,
	EC_LIB_NB_CANDIDATE_EDIT_ERROR,
	EC_LIB_NB_OPERATIONAL_DATA,
	EC_LIB_NB_TRANSACTION_CREATION_FAILED,
	EC_LIB_NB_TRANSACTION_RECORD_FAILED,
	EC_LIB_LIBYANG,
	EC_LIB_LIBYANG_PLUGIN_LOAD,
	EC_LIB_CONFD_INIT,
	EC_LIB_CONFD_DATA_CONVERT,
	EC_LIB_LIBCONFD,
	EC_LIB_SYSREPO_INIT,
	EC_LIB_SYSREPO_DATA_CONVERT,
	EC_LIB_LIBSYSREPO,
	EC_LIB_GRPC_INIT,
	EC_LIB_ID_CONSISTENCY,
	EC_LIB_ID_EXHAUST,
	EC_LIB_RESOLVER,
};

extern void lib_error_init(void);

#ifdef __cplusplus
}
#endif

#endif

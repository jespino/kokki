
__description__ = "MongoDB database"
__config__ = {
    "mongodb.dbpath": dict(
        description = "Path where to store the MongoDB database",
        default = "/var/lib/mongodb",
    ),
    "mongodb.logpath": dict(
        description = "Path where to store the MongoDB log",
        default = "/var/log/mongodb/mongodb.log",
    ),
    "mongodb.verbose": dict(
        description = "Verbose logging output",
        default = False,
    ),
    "mongodb.oplog_size": dict(
        description = "Custom size for replication operation log.",
        default = None,
    ),
    "mongodb.op_id_mem": dict(
        description = "Size limit for in-memory storage of op ids.",
        default = None,
    ),
    "mongodb.replica_set": dict(
        description = "<setname>[/<seedlist>] Use replica sets with the specified logical set name.  Typically the optional seed host list need not be specified."
        default = None,
    ),
}

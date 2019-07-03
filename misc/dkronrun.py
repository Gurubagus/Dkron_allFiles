"""
Command line options:

--node-name - Name of the node, must be unique in the cluster. By default this is the hostname of the machine.

--bind-addr - The address that dkron will bind to for communication with other dkron nodes. By default this is 0.0.0.0:8946. dkron nodes may have different ports. If a join is specified without a port, we default to locally configured port. dkron uses both TCP and UDP and use the same port for both, so if you have any firewalls be sure to allow both protocols. If this configuration value is changed and no port is specified, the default of 8946 will be used.

--join - Address of another agent to join upon starting up. This can be specified multiple times to specify multiple agents to join. If Dkron is unable to join with any of the specified addresses, agent startup will fail. By default, the agent won't join any nodes when it starts up.

--advertise-addr - The advertise flag is used to change the address that we advertise to other nodes in the cluster. By default, the bind address is advertised. However, in some cases (specifically NAT traversal), there may be a routable address that cannot be bound to. This flag enables gossiping a different address to support this. If this address is not routable, the node will be in a constant flapping state, as other nodes will treat the non-routability as a failure.

--http-addr - The address where the web UI will be binded. By default :8080

--backend - Backend storage to use, etcd, consul, zk (zookeeper) or redis. The default is etcd.

--backend-machine - Backend storage servers addresses to connect to. This flag can be specified multiple times. By default 127.0.0.1:2379

--tag - The tag flag is used to associate a new key/value pair with the agent. The tags are gossiped and can be used to provide additional information such as roles, ports, and configuration values to other nodes. Multiple tags can be specified per agent. There is a byte size limit for the maximum number of tags, but in practice dozens of tags may be used. Tags can be changed during a config reload.

--server - If this agent is a dkron server, just need to be present. Absent by default.

--keyspace - Keyspace to use for the store. Allows to run different instances using the same storage cluster. dkron by default.

--encrypt - Key for encrypting network traffic. Must be a base64-encoded 16-byte key.

--mail-host - Mail server host address to use for notifications.

--mail-port - Mail server port.

--mail-username - Mail server username used for authentication.

--mail-password - Mail server password to use.

--mail-from - From email address to use.

--webhook-url - Webhook url to call for notifications.
"""

import os

cmd = 'dkron agent --server --backend-machine 0.0.0.0:2379 --backend etcd --node-name Dkron_Main bg'

if __name__=='__main__':

	os.system(cmd)

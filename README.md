# Distributed-Key-Value-Store-using-etcd
This project is a distributed key-value store created using etcd and a python backend.<br />

It was done with a team of 4 for a Cloud Computing project at PES University.

# Project Details
The user interacts with a simple flask front end, where key values can be entered, deleted and listed out.<br />

The backend ensures:
1. Storage of key-value pairs by connecting to one of the operational nodes in the etcd cluster.
2. Replication of key-value pairs across the cluster for fault tolerance and consistency.

## Architecture

<img width="1126" alt="Screenshot 2024-10-16 at 2 44 32 PM" src="https://github.com/user-attachments/assets/37673271-2dc4-4cd3-8797-46528852d15a"><br />

As seen in the diagram, the etcd client will take care of interacting with etcd. The cluster will ensure that<br />
any insertion is replicated across the nodes in the cluster which means that the system can handle one node failing.

## What is etcd
etcd is a distributed, reliable key-value store designed for high availability, consistency, and performance. <br />
It is commonly used for storing configuration data, service discovery, and coordinating distributed systems.

[etcd Documentation](https://etcd.io/docs/v3.5/)

## Raft Consensus

It has to be noted that since there are three nodes in the cluster, only one failure can be handled. If there<br />
is a need for better failure tolerance, more nodes can be configured.<br />

This is due to the need for a majority in order to reach consensus. Since etcd utilises Raft, which works on a<br />
quorum based approach.<br /><br />

For a cluster of N nodes: A majority of [N/2] nodes must agree to achieve consensus.<br />
The system can tolerate up to [(N - 1)/2] faulty nodes.<br /><br />

The table below gives a few examples on quorum size and tolerable failures:
<br />

| Number of Nodes (N) | Quorum Size ([N/2]) | Tolerated Failures ([(N-1)/2]) |
|----------------------|---------------------|--------------------------------|
| 3                    | 2                   | 1                              |
| 5                    | 3                   | 2                              |
| 7                    | 4                   | 3                              |

<img width="994" alt="Screenshot 2024-10-16 at 2 44 46 PM" src="https://github.com/user-attachments/assets/1eac76ac-8226-4c31-b2e9-46b7ebb61dc5">

As seen in the above image, for a cluster with three nodes if a failure occurs the system will continue to<br />
function without any problems, and no key values will be lost.<br /><br />
This particular system would be down if 2 failures occur but the number of nodes in the cluster can be <br />
configured according to thee users needs. 

# How to Run

## Pre-Requirements
- OS: Linux/MacOS
- etcd (version: 3.5.12)
- Python 3.11+
- etcd3 module (pip install etcd3)

## Execution
- Make appropriate changes to any file that requires changes i.e. ip address or dir path
- Start the cluster using (./cluster.sh)
- Make sure the nodes are up and running, then use the command (./run.sh)
- Open a browser window and use the application on <http://127.0.0.1:5000>
- To run the tests, execute (./test.sh) in a terminal window

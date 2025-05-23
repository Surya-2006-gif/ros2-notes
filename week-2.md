# WEEK -2
---
# DDS

(Data Distribution system),from the abbrevation we can understand something right it is a sytem or service for data distribution.



###  **What does a DDS exactly do??**

    - So this is a industrial standard software/middleware  for efficient and reliable communication between systems and nodes. 

    - So in ros2 when we use its API,it triggers some communication process via which two nodes identify and communicate


### **How is the workflow when we use ros2 API??**
 
 ROS 2 → RCL(ros2 client library) → RMW → DDS

let us not focus much on RCL we shall see briefly about RMW and go on to DDS

**RMW:**
- It is the software layer between dds implementations and ros2 client libraries.

- So in simple words, RMW lets ROS 2 talk to different middleware systems without having to change your ROS 2 code. It takes care of converting ROS messages and commands into a format that the middleware understands

**DDS:**

    - Similar to our publisher and subscriber which communicates via a topic ,dds communications also take places in the similar analogical way

- In the backend DDS takes care all of these,

       - Discovery 
       - Data serialization
       - QoS policies 
       - Transport layer 
       - Peer-to-peer communication

let us explain this along way we discuss further,



 - So what happens inside DDS  when we create a node/service/action or use inbuilt APIs like topic list...etc.


    - _let us take a example of creating a publisher and subscriber node_.
       
          - First for each node, a domain entity  called DomainParticipant(It is the entry point.) is created which is assigned a domain ID(It is assigned before a node startup).Similar property nodes(such as a publisher and subscriber of same topic are given same ID).

          - So for each dataparticipant one or more publisher and /or subscriber are created  inside which we have one or more datawriters and /or datareaders respectively

          - these datawriters/datasubscribers is associated with a specific topic.So these topic are localised to that DomainParticipant

          - so nodes find each other by discovery then establish a peer-to-peer connection.


#### What is discovery??
 This our structure,
  
    DomainParticipant
    └── Publisher
         └── DataWriter (→ topic A)
    └── Subscriber
         └── DataReader (→ topic A)

So discovery (these are local to a domain) helps to find DataWriters find matching DataReaders, and vice versa — based on:

    - Topic name

    - Data type

    - QoS policies


We have Two phases while discovery

    - SPDP(Simple Participant Discovery Protocol):

        --> This protocol ensures all DomainParticipants of the same domain get to know eachother
       
        --> Each DomainParticipants send announcments periodically to other Participants in the same domain.The details include the DomainParticipant’s unique identifying key (GUID or Globally Unique ID described below), transport locators (addresses and port numbers), and QoS.

        --> This periodicity of messages also the 'liveliness' of the DomainParticipant.These messages are sent on a periodic basis using best-effort communication. ( The announcements are sent using best-effort reliability, meaning they are not guaranteed to be delivered, but are sent repeatedly to increase the likelihood of reception)

        --> When a DomainParticipant is deleted, a dispose participant message with the DomainParticipant's identifying GUID is sent.

    - SEDP(Simple Endpoint Discovery Protocol):

        --> So using spdp each participant is familiar with each other using sedp endpoints get to know each other (especially the DataWriters and thr DataPublishers)

        -->  Once two DomainParticipants have discovered each other via SPDP, SEDP takes over to exchange metadata about all DataWriters and DataReaders (endpoints) each participant owns

        --> Participants send publication DATA messages (for DataWriters) and subscription DATA messages (for DataReaders). These messages include the endpoint’s GUID, topic name, data type, and relevant QoS policies

        --> Each participant matches remote DataWriters and DataReaders with its own endpoints based on topic, data type, and compatible QoS. Only matching endpoints are connected for data exchange


 - Okay so far we've matched datawriters and datareaders but how does the communication happen and what is the the communication type.

       - PEER-TO-PEER LINK ESTABLISHED:

          - The DDS participants create a direct communication channel(Publisher (DataWriter) sends messages directly to the matched subscriber (DataReader))

          - The messages are not sent in the same format instead, they are serialised( into a stream of bytes for transmission between datawriters and datareaders),then it is deserialsed after it reaches datareaders


#### What is a udp(user datagram protocol)??
        
        - UDP is transport protocol(in a Transport layer) 

        - It is a protocol for commuication between two nodes.It is connectionless(he sender can send data without setting up a dedicated connection with the receiver beforehand.)Even though UDP is connectionless, the destination is known because:

              Every UDP packet includes:

                   The destination IP address

                   The destination port number


        
        - Let us say our Node A wants to communicate with Node B.UDP works as a postman for it.So first a message is serialized,then we sent it via a UDP.
        
        - This UDP doesnt reliably send messages meaning it doesnt care if packets of data(as a result of serialization) reaches the destinatoin correctly.It aims to transfer these packes fast enough.

        - It is used in spdp,sedp(both of these uses multicast udp),communication of datawriters and datareaders(uses unicast udp)

        - Unicast UDP sends data from one sender to one specific receiver using a direct IP address—it's a one-to-one communication. In contrast, Multicast UDP sends data from one sender to multiple receivers who have joined a multicast group—it's a one-to-many communication


 - RTPS is a set of rules that helps DDS send messages between computers quickly and reliably. RTPS is the full communication protocol used by DDS that includes discovery, data exchange, and other parts like message formatting and reliability.

 - It uses UDP as the transport method to send the actual packets over the network. So, discovery, data serialization, QoS, and peer-to-peer communication are all parts of what RTPS handles—while UDP is just the underlying way those messages get physically sent from one computer to another.



#### **We have a alternative to simple discovery at times when needed called the Discovery Server**

- Simple discovery server is  decentralised (peer-to-peer) communication and it requires multicast communication

- While a discovery server uses  a centralized server-based discovery model.

- Instead of nodes broadcasting to everyone, each node registers itself with a centralized Discovery Server.

- The server keeps a list of all nodes and tells nodes about others only when needed. Nodes only talk to the server for discovery, not to every node.

### What is a ros master??
  A ROS Master is a central part of ROS 1 that helps all the robot’s nodes find and connect to each other. When a node starts, it tells the Master what topics it wants to publish or subscribe to. The Master keeps track of this info and helps nodes discover each other so they can communicate directly.The Master runs as a single program (roscore) and acts like a phone book for nodes. Without it, nodes wouldn’t know where to send or get data, so the system wouldn’t work properly.

### Why was the ros master dropped???

It was dropped of the following reasons:

      - The ROS Master acts as a central server, so if it goes down or restarts, all nodes lose connection and communication breaks

      - 
  



        


        




# ROS2 - Notes

## Week - 1
   getting started and exploring ROS2


1.**What are _Nodes_??**

     1. Nodes are smallest executable program parts which has a specific task to be done.
     2. All nodes work independently(One cannot call others parameters or call other nodes) although they can communicate with one another using messages,services and actions.
     3. Nodes are created within packages which are inside src folder of ros2 workspace


[For more functionalities on nodes](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html)

---
2.**What are Messages???**

     One node communicates with the other  using messages via a communication channel. There are some std.
    
[---> click here <---](https://github.com/ros2/common_interfaces)    to see some common messages

---
#### There are 3 communication channels
  - **Topic**
           
        - This is the most typical way of two nodes communicating.
        - Here a publisher node publishes messages into this and whichever node wants to get that message can subscribe to this and can access them.

![Topic-SinglePublisherandSingleSubscriber](https://github.com/user-attachments/assets/67ef3aa3-8ce1-470f-a7e2-085cdb9470a1)

A node may publish data to any number of topics and simultaneously have subscriptions to any number of topics.

![Topic-MultiplePublisherandMultipleSubscriber](https://github.com/user-attachments/assets/1f565f8f-299e-4678-bac8-96a409b1933d)

[for more functionalities on Topic](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html)

---
  - **Service**
         
         - Even though topics are a widely used channel for messages, sometimes we need services, which work based on a request-response type, unlike the continual messages and data published to topics.
         - Here, a client node makes a request, and the server node (or service node) gives back a response.
         - This is useful when you want to trigger something once — like turning on a motor, resetting a sensor, or asking for a specific value — rather than streaming data all the time like in topics.

![Service-SingleServiceClient](https://github.com/user-attachments/assets/1ff5fcba-aa6e-44de-b28e-d5359314ebe6)

![Service-MultipleServiceClient](https://github.com/user-attachments/assets/3fa30b5f-634c-4615-a28f-74e1cd842309)

[for more functionalities on service](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services.html)

---

 - **Action**

       - Even though services are great for quick request-response interactions, sometimes we need something more flexible — that’s where actions come in.
       - Actions are used when the task takes a long time to complete and you still want to get feedback in between, instead of just waiting for the final result like in services.
       - Here, a client node sends a goal to the action server (like “go to this location” or “pick up this object”), and the action server node keeps sending feedback, and once it's done, it sends back the result.
         So it's a mix of:
             - Sending a goal like a service,
             - Getting continuous feedback like a topic,
             And finally getting a result when the task is complete.

![Action-SingleActionClient](https://github.com/user-attachments/assets/2e348877-790d-4d8b-9dc2-b2379b90e616)

[for more functionalities on action](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Actions/Understanding-ROS2-Actions.html)

---

### Analyzing the program for the week(1):

#### The Publisher Node :

![Screenshot 2025-05-17 114441](https://github.com/user-attachments/assets/1d81efcf-29d6-48ac-b68a-dbb1518135ba)


**So you see this part in most of the code for nodes,but what exactly is this??**

![Screenshot 2025-05-17 114616](https://github.com/user-attachments/assets/9e629cea-fffb-4696-b0f5-41757cf9546e)

- So this tells the Python interpreter to start calling the `main()` function only if the script is run directly from its original place — like running the file from the t nal or launching it with `ros2 run`.
- If the script is imported into some other file, then this part won’t execute.

![Screenshot 2025-05-17 114923](https://github.com/user-attachments/assets/43c0f47a-8bb6-4ee3-9636-2fe18101428c)


- The above will be the common structure for any `main()`  you will create.

- The `main()` is the “Entry point” for running a node.Inside it you have to enable ros2 communications and set up the environment using `rclpy.init(args=args)`

- After performing certain methods you have to delete node using `<instance name>.destroy_node()` and disable ros2 communications using `rclpy.shutdown()`



---

- Typically the Nodes and its methods are created using OOPS.The parent class of it should be the class `Node` from `rclpy.node`


- To create a publisher there is a method available called `create_publisher(msg_type,Topic_name,Queue)`
---

- The `queue_size` is important when the subscriber can't keep up with the messages being published.
- Let’s say your publisher is sending messages very fast, but the subscriber is a bit slow or busy — this queue stores the last few messages temporarily.
- If the queue is full, old messages get dropped.
---

- `get_logger().info(...)`  – This prints the message in the Terminal along with timestamp and node name

#### The subscriber node:


![Screenshot 2025-05-17 115741](https://github.com/user-attachments/assets/7e41fe1f-65bf-410b-9bb0-1bab449d6ee4)

- **What is listener_callback and when is it called?**

      - listener_callback is a callback function — this means it is a special function that gets called automatically by ROS 2 whenever a new message arrives on the subscribed topic ('chatter' in this case).
      - Whenever the node receives a Float32 message published on the 'chatter' topic, ROS 2 triggers the listener_callback function and passes the received message as the argument msg.
      - Inside this function, you can define what you want to do with the incoming data. Here, it prints the message value and its square using get_logger().info().

- **What about the timer and its callback?**

   - The timer is created using `create_timer(interval_in_seconds, callback_function).`
   - It calls the callback function repeatedly at a fixed interval (every 0.5 seconds here).
   - In this code, the timer calls `check_for_publisher` every 0.5 seconds. This callback checks if any message has been received yet (self.msg_received). If not, it prints a warning to let the user know that no message has arrived. Once a message arrives, the timer is cancelled to stop this periodic checking.

- **What is `rclpy.spin(node)`?**

      - rclpy.spin(node) keeps your node alive and running continuously.
      - It starts an event loop that waits for any callbacks (like subscriber callbacks, timers, services) to happen, and executes them whenever they are triggered.
      - Your program keeps running until you manually stop it or shut down ROS 2.

- **What is `rclpy.spin_once(node)`?**

      - rclpy.spin_once(node) processes only one round of callbacks and then returns immediately.
      - It checks if there are any callbacks ready to run at that moment, runs them, and then exits.
      - It does not keep your node alive; you need to call it repeatedly (usually inside a loop) if you want continuous processing.

- **What is a namespace?**

  - When two same nodes are launched (like two instances of the same code), they might try to publish or subscribe to the same topic or have the same node name, which leads to a conflict.To avoid this, we use namespaces 
  -    It prefixes names so that there are no conflicts when multiple nodes use the same topic or service names.
  -  `ros2 run <pkg> <node> --ros-args -r __ns:=/my_namespace` --->  for running a node with a namepsace

# WEEK-2
----

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


        
# WEEK -3

## Brief Explanation

![image](https://github.com/user-attachments/assets/4f34c3ba-c7d9-44fd-b037-c20fc3e44cc9)


## Differential drive controller:

 - I have created diff-drive-controller only for the rear wheels.

 - The `/differential_drive_controller` node subscribes to `/cmd_vel` where it hears the Twist message published.

 - Hearing from the Twist message the bot moves accordingly

 - The `/differential_drive_controller` publishes msg into `odom` topic of type `nav_msgs/msg/Odometry` using which we can see the tf of the base_link w.r.t to gazebo origin



 ## Camera Plugin:

 - The node `/camera_plugin` publishes to two topics `my_camera/camera_info` and `/my_camera/image_raw`


 - `/my_camera/image_raw` is topic where the `sensor_msgs/Image` is published.If subscribed to this topic we could use the camera's output

 - `my_camera/camera_info` topic has messages regarding the callibration of camera 

 ## Lidar Plugin

 - This plugin simulates a virtual Lidar

 - The node `/lidar_controller` publishes the output of the virtual sensor to the topic `/scan` of type `sensor_msgs/LaserScan`

---
## Stopper_node:

 - Our `/stopper_node`  stops the bot if the horizontal distance becomes less than or equal to 0.5 m 
 
 - `/stopper_node` subscribes to  `/scan` topic goes through the message.Even if a single ray's distance is >=0.5 publishes a msg to `/cmd_vel`.(a Twist msg contain linear and angular velocities as '0')


 ## How to a run the node??

- I have created a launch file for spawning a robot in gazebo

```
 ros2 launch my_robot_description gazebo_sim.launch.py
```


- To use a stopper_node in another terminal 

```
 ros2 run lidar_based_contoller lidar_stopper 
```


# Video Link Of Robot Simulation:

- https://drive.google.com/drive/folders/18fmEQMbYiqsGDM2ieHdm06u7pteD4Q0Y?usp=sharing
        



   















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

![Topic-SinglePublisherandSingleSubscriber](https://github.com/user-attachments/assets/87897d1b-8ac0-441a-89b6-f6e3093562b1)

A node may publish data to any number of topics and simultaneously have subscriptions to any number of topics.

![Topic-MultiplePublisherandMultipleSubscriber](https://github.com/user-attachments/assets/3089da34-93b3-4f9d-ab04-1d9f9e292ac3)

[for more functionalities on Topic](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html)

---
  - **Service**
         
         - Even though topics are a widely used channel for messages, sometimes we need services, which work based on a request-response type, unlike the continual messages and data published to topics.
         - Here, a client node makes a request, and the server node (or service node) gives back a response.
         - This is useful when you want to trigger something once — like turning on a motor, resetting a sensor, or asking for a specific value — rather than streaming data all the time like in topics.

![Service-SingleServiceClient](https://github.com/user-attachments/assets/170a72e0-f569-4aeb-806a-11afaa1ee6dd)

![Service-MultipleServiceClient](https://github.com/user-attachments/assets/9e3c547d-84e1-43d1-9e4c-9b4c1dc10d95)

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

![Action-SingleActionClient](https://github.com/user-attachments/assets/85cf3721-5732-42ba-8955-005b49311e12)

[for more functionalities on action](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Actions/Understanding-ROS2-Actions.html)

---

### Analyzing the program for the week(1):

#### The Publisher Node :

![Screenshot 2025-05-17 114441](https://github.com/user-attachments/assets/f56daddf-28a2-49d6-b5c3-03f78518aa3b)

**So you see this part in most of the code for nodes,but what exactly is this??**

![Screenshot 2025-05-17 114616](https://github.com/user-attachments/assets/f50923b0-de5c-45b3-adcb-06eada452748)

- So this tells the Python interpreter to start calling the `main()` function only if the script is run directly from its original place — like running the file from the t nal or launching it with `ros2 run`.
- If the script is imported into some other file, then this part won’t execute.

![Screenshot 2025-05-17 114923](https://github.com/user-attachments/assets/36ee5ba2-8565-4da9-8a84-92b6bda1246c)


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


![Screenshot 2025-05-17 115741](https://github.com/user-attachments/assets/84c8edbd-febd-4c9f-bbc3-fb1e8769c230)

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





   














{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "32145e5a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#ROS NOETIC UBUNTU  20 PYTHON3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6c54ce57",
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "cannot import name 'Twist' from 'geometry_msgs' (/opt/ros/noetic/lib/python3/dist-packages/geometry_msgs/__init__.py)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "Input \u001b[0;32mIn [1]\u001b[0m, in \u001b[0;36m<cell line: 4>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mtime\u001b[39;00m\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mnumpy\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mnp\u001b[39;00m \n\u001b[0;32m----> 4\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mgeometry_msgs\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Twist\n",
      "\u001b[0;31mImportError\u001b[0m: cannot import name 'Twist' from 'geometry_msgs' (/opt/ros/noetic/lib/python3/dist-packages/geometry_msgs/__init__.py)"
     ]
    }
   ],
   "source": [
    "import rospy \n",
    "import time\n",
    "import numpy as np \n",
    "from geometry_msgs import Twist\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "afd1e2ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Unable to load msg [geometry_msgs/Twis]: Cannot locate message [Twis] in package [geometry_msgs] with paths [['/opt/ros/noetic/share/geometry_msgs/msg']]\r\n"
     ]
    }
   ],
   "source": [
    "! rosmsg info geometry_msgs/Twis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "98e47c48",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'rospy' has no attribute 'publisher'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Input \u001b[0;32mIn [4]\u001b[0m, in \u001b[0;36m<cell line: 2>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m rospy\u001b[38;5;241m.\u001b[39minit_node (\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mbase_and_sensor\u001b[39m\u001b[38;5;124m'\u001b[39m)  \u001b[38;5;66;03m###conectamos/creamoos un nodo llamado \u001b[39;00m\n\u001b[0;32m----> 2\u001b[0m base_vel_pub \u001b[38;5;241m=\u001b[39m \u001b[43mrospy\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mpublisher\u001b[49m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m/hsrb/command_velocity\u001b[39m\u001b[38;5;124m'\u001b[39m,Twist, queue_size)\n",
      "\u001b[0;31mAttributeError\u001b[0m: module 'rospy' has no attribute 'publisher'"
     ]
    }
   ],
   "source": [
    "rospy.init_node ('base_and_sensor')  ###conectamos/creamoos un nodo llamado \n",
    "base_vel_pub = rospy.publisher('/hsrb/command_velocity',Twist, queue_size=10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "af03fa7a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def move_base_vel(vx, vy, vw):\n",
    "    twist = Twist()\n",
    "    twist.linear.x = vx\n",
    "    twist.linear.y = vy\n",
    "    twist.angular.z = vz\n",
    "    base_vel_pub.publish(twist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e90ba125",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'twist' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [4]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mtwist\u001b[49m\u001b[38;5;241m.\u001b[39mlinear\u001b[38;5;241m.\u001b[39my\n",
      "\u001b[0;31mNameError\u001b[0m: name 'twist' is not defined"
     ]
    }
   ],
   "source": [
    "twist.linear.y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0a0d056c",
   "metadata": {},
   "outputs": [
    {
     "ename": "ROSInitException",
     "evalue": "time is not initialized. Have you called init_node()?",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mROSInitException\u001b[0m                          Traceback (most recent call last)",
      "Input \u001b[0;32mIn [5]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0m start_time \u001b[38;5;241m=\u001b[39m \u001b[43mrospy\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mTime\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mnow\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241m.\u001b[39mto_sec()\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m rospy\u001b[38;5;241m.\u001b[39mTime\u001b[38;5;241m.\u001b[39mnow()\u001b[38;5;241m.\u001b[39mto_sec() \u001b[38;5;241m-\u001b[39m start_time \u001b[38;5;241m<\u001b[39m \u001b[38;5;241m30\u001b[39m:\n\u001b[1;32m      3\u001b[0m     move_base_vel(\u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m0.1\u001b[39m, \u001b[38;5;241m0\u001b[39m)\n",
      "File \u001b[0;32m/opt/ros/noetic/lib/python3/dist-packages/rospy/rostime.py:155\u001b[0m, in \u001b[0;36mTime.now\u001b[0;34m()\u001b[0m\n\u001b[1;32m    143\u001b[0m \u001b[38;5;129m@staticmethod\u001b[39m\n\u001b[1;32m    144\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mnow\u001b[39m():\n\u001b[1;32m    145\u001b[0m     \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    146\u001b[0m \u001b[38;5;124;03m    Create new L{Time} instance representing current time. This\u001b[39;00m\n\u001b[1;32m    147\u001b[0m \u001b[38;5;124;03m    can either be wall-clock time or a simulated clock. It is\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    153\u001b[0m \u001b[38;5;124;03m    @rtype: L{Time}\u001b[39;00m\n\u001b[1;32m    154\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[0;32m--> 155\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mget_rostime\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m/opt/ros/noetic/lib/python3/dist-packages/rospy/rostime.py:190\u001b[0m, in \u001b[0;36mget_rostime\u001b[0;34m()\u001b[0m\n\u001b[1;32m    184\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    185\u001b[0m \u001b[38;5;124;03mGet the current time as a L{Time} object    \u001b[39;00m\n\u001b[1;32m    186\u001b[0m \u001b[38;5;124;03m@return: current time as a L{rospy.Time} object\u001b[39;00m\n\u001b[1;32m    187\u001b[0m \u001b[38;5;124;03m@rtype: L{Time}\u001b[39;00m\n\u001b[1;32m    188\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    189\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m _rostime_initialized:\n\u001b[0;32m--> 190\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m rospy\u001b[38;5;241m.\u001b[39mexceptions\u001b[38;5;241m.\u001b[39mROSInitException(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtime is not initialized. Have you called init_node()?\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m    191\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m _rostime_current \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m    192\u001b[0m     \u001b[38;5;66;03m# initialize with sim time\u001b[39;00m\n\u001b[1;32m    193\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m _rostime_current\n",
      "\u001b[0;31mROSInitException\u001b[0m: time is not initialized. Have you called init_node()?"
     ]
    }
   ],
   "source": [
    "start_time = rospy.Time.now().to_sec()\n",
    "while rospy.Time.now().to_sec() - start_time < 30:\n",
    "    move_base_vel(0, -0.1, 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e39c751e",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'twist' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [6]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mtwist\u001b[49m\u001b[38;5;241m.\u001b[39mlinear\u001b[38;5;241m.\u001b[39mx\n",
      "\u001b[0;31mNameError\u001b[0m: name 'twist' is not defined"
     ]
    }
   ],
   "source": [
    "twist.linear.x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fedd4d45",
   "metadata": {},
   "outputs": [
    {
     "ename": "ROSInitException",
     "evalue": "time is not initialized. Have you called init_node()?",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mROSInitException\u001b[0m                          Traceback (most recent call last)",
      "Input \u001b[0;32mIn [7]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0m start_time \u001b[38;5;241m=\u001b[39m \u001b[43mrospy\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mTime\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mnow\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241m.\u001b[39mto_sec()\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m rospy\u001b[38;5;241m.\u001b[39mTime\u001b[38;5;241m.\u001b[39mnow()\u001b[38;5;241m.\u001b[39mto_sec() \u001b[38;5;241m-\u001b[39m start_time \u001b[38;5;241m<\u001b[39m \u001b[38;5;241m50\u001b[39m:\n\u001b[1;32m      3\u001b[0m     move_base_vel(\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m0.1\u001b[39m, \u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m0\u001b[39m)\n",
      "File \u001b[0;32m/opt/ros/noetic/lib/python3/dist-packages/rospy/rostime.py:155\u001b[0m, in \u001b[0;36mTime.now\u001b[0;34m()\u001b[0m\n\u001b[1;32m    143\u001b[0m \u001b[38;5;129m@staticmethod\u001b[39m\n\u001b[1;32m    144\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mnow\u001b[39m():\n\u001b[1;32m    145\u001b[0m     \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    146\u001b[0m \u001b[38;5;124;03m    Create new L{Time} instance representing current time. This\u001b[39;00m\n\u001b[1;32m    147\u001b[0m \u001b[38;5;124;03m    can either be wall-clock time or a simulated clock. It is\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    153\u001b[0m \u001b[38;5;124;03m    @rtype: L{Time}\u001b[39;00m\n\u001b[1;32m    154\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[0;32m--> 155\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mget_rostime\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m/opt/ros/noetic/lib/python3/dist-packages/rospy/rostime.py:190\u001b[0m, in \u001b[0;36mget_rostime\u001b[0;34m()\u001b[0m\n\u001b[1;32m    184\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    185\u001b[0m \u001b[38;5;124;03mGet the current time as a L{Time} object    \u001b[39;00m\n\u001b[1;32m    186\u001b[0m \u001b[38;5;124;03m@return: current time as a L{rospy.Time} object\u001b[39;00m\n\u001b[1;32m    187\u001b[0m \u001b[38;5;124;03m@rtype: L{Time}\u001b[39;00m\n\u001b[1;32m    188\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    189\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m _rostime_initialized:\n\u001b[0;32m--> 190\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m rospy\u001b[38;5;241m.\u001b[39mexceptions\u001b[38;5;241m.\u001b[39mROSInitException(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtime is not initialized. Have you called init_node()?\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m    191\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m _rostime_current \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m    192\u001b[0m     \u001b[38;5;66;03m# initialize with sim time\u001b[39;00m\n\u001b[1;32m    193\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m _rostime_current\n",
      "\u001b[0;31mROSInitException\u001b[0m: time is not initialized. Have you called init_node()?"
     ]
    }
   ],
   "source": [
    "start_time = rospy.Time.now().to_sec()\n",
    "while rospy.Time.now().to_sec() - start_time < 50:\n",
    "    move_base_vel(-0.1, 0, 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5f63f4a2",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'twist' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [8]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mtwist\u001b[49m\u001b[38;5;241m.\u001b[39mlinear\u001b[38;5;241m.\u001b[39my\n",
      "\u001b[0;31mNameError\u001b[0m: name 'twist' is not defined"
     ]
    }
   ],
   "source": [
    "twist.linear.y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "26f6b1ae",
   "metadata": {},
   "outputs": [
    {
     "ename": "ROSInitException",
     "evalue": "time is not initialized. Have you called init_node()?",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mROSInitException\u001b[0m                          Traceback (most recent call last)",
      "Input \u001b[0;32mIn [9]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0m start_time \u001b[38;5;241m=\u001b[39m \u001b[43mrospy\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mTime\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mnow\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241m.\u001b[39mto_sec()\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m rospy\u001b[38;5;241m.\u001b[39mTime\u001b[38;5;241m.\u001b[39mnow()\u001b[38;5;241m.\u001b[39mto_sec() \u001b[38;5;241m-\u001b[39m start_time \u001b[38;5;241m<\u001b[39m \u001b[38;5;241m7\u001b[39m:\n\u001b[1;32m      3\u001b[0m     move_base_vel(\u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m0.1\u001b[39m, \u001b[38;5;241m0\u001b[39m)\n",
      "File \u001b[0;32m/opt/ros/noetic/lib/python3/dist-packages/rospy/rostime.py:155\u001b[0m, in \u001b[0;36mTime.now\u001b[0;34m()\u001b[0m\n\u001b[1;32m    143\u001b[0m \u001b[38;5;129m@staticmethod\u001b[39m\n\u001b[1;32m    144\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mnow\u001b[39m():\n\u001b[1;32m    145\u001b[0m     \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    146\u001b[0m \u001b[38;5;124;03m    Create new L{Time} instance representing current time. This\u001b[39;00m\n\u001b[1;32m    147\u001b[0m \u001b[38;5;124;03m    can either be wall-clock time or a simulated clock. It is\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    153\u001b[0m \u001b[38;5;124;03m    @rtype: L{Time}\u001b[39;00m\n\u001b[1;32m    154\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[0;32m--> 155\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mget_rostime\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m/opt/ros/noetic/lib/python3/dist-packages/rospy/rostime.py:190\u001b[0m, in \u001b[0;36mget_rostime\u001b[0;34m()\u001b[0m\n\u001b[1;32m    184\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    185\u001b[0m \u001b[38;5;124;03mGet the current time as a L{Time} object    \u001b[39;00m\n\u001b[1;32m    186\u001b[0m \u001b[38;5;124;03m@return: current time as a L{rospy.Time} object\u001b[39;00m\n\u001b[1;32m    187\u001b[0m \u001b[38;5;124;03m@rtype: L{Time}\u001b[39;00m\n\u001b[1;32m    188\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    189\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m _rostime_initialized:\n\u001b[0;32m--> 190\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m rospy\u001b[38;5;241m.\u001b[39mexceptions\u001b[38;5;241m.\u001b[39mROSInitException(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtime is not initialized. Have you called init_node()?\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m    191\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m _rostime_current \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m    192\u001b[0m     \u001b[38;5;66;03m# initialize with sim time\u001b[39;00m\n\u001b[1;32m    193\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m _rostime_current\n",
      "\u001b[0;31mROSInitException\u001b[0m: time is not initialized. Have you called init_node()?"
     ]
    }
   ],
   "source": [
    "start_time = rospy.Time.now().to_sec()\n",
    "while rospy.Time.now().to_sec() - start_time < 7:\n",
    "    move_base_vel(0, -0.1, 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "9b6302da",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'twist' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [10]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mtwist\u001b[49m\u001b[38;5;241m.\u001b[39mangular\u001b[38;5;241m.\u001b[39mz\n",
      "\u001b[0;31mNameError\u001b[0m: name 'twist' is not defined"
     ]
    }
   ],
   "source": [
    "twist.angular.z"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4db8cea0",
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = rospy.Time.now().to_sec()\n",
    "while rospy.Time.now().to_sec() - start_time < 9:\n",
    "    move_base_vel(0, 0, 0.1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0ece419",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

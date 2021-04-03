
//written by Hariharan <A.H.N>
#include <ros.h>
#include <std_msgs/Float32.h>
#define ep 2
#define tp 3
long distance;
long duration;
ros::NodeHandle  nh;

std_msgs::Float32 str_msg;
ros::Publisher sensor("sensor", &str_msg);


void setup()
{
  pinMode(tp,OUTPUT);
  pinMode(ep , INPUT);
 
  nh.initNode();
  nh.advertise(sensor);
}

void loop()
{
  digitalWrite(tp , LOW);
  delayMicroseconds(2);
  digitalWrite(tp, HIGH);
  delayMicroseconds(10);
  digitalWrite(tp , LOW);
  duration = pulseIn(ep , HIGH);
  distance = duration *0.034/2;
  
  str_msg.data = distance;
  sensor.publish( &str_msg );
  nh.spinOnce();
  delay(100);
}

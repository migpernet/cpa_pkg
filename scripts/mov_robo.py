#!/usr/bin/env python3

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def move_ur5():
    # Inicialize o nó ROS
    rospy.init_node('ur5_trajectory_control', anonymous=True)
    # Configura o publisher para o tópico de controle do UR5
    pub = rospy.Publisher('/ur5/eff_joint_traj_controller/command', JointTrajectory, queue_size=10)
    
    # Crie a mensagem de trajetória
    trajectory_msg = JointTrajectory()
    trajectory_msg.joint_names = ["shoulder_pan_joint", "shoulder_lift_joint", 
                                  "elbow_joint", "wrist_1_joint", 
                                  "wrist_2_joint", "wrist_3_joint"]
    
    # Defina o ponto da trajetória (posição de destino das juntas)
    point = JointTrajectoryPoint()
    point.positions = [0.0, -1.57, 0.0, 0.0, 0.0, -1.57]  # Posições das juntas
    #point.positions = [0.0, -1.56, 1.14, 0.05, 0.0, -2.77]  # Posições das juntas
    point.time_from_start = rospy.Duration(2)  # Tempo em segundos para alcançar a posição
    
    # Adicione o ponto à mensagem de trajetória
    trajectory_msg.points = [point]
    
    # Publique a trajetória no tópico
    rospy.sleep(1)  # Pequeno delay para garantir que o nó está ativo
    pub.publish(trajectory_msg)
    rospy.loginfo("Mensagem de movimento enviada para o UR5")

if __name__ == '__main__':
    try:
        move_ur5()
    except rospy.ROSInterruptException:
        pass


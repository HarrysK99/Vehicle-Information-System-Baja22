#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main(int argc, char** argv)
{
    if(argc != 2) {
        printf("Usage : %s HOME_PATH\n", argv[0]);
    }
    pid_t roscore = fork();
    if(roscore == 0) {
        execl("/bin/sh", "sh", strcat(argv[1], "/autoexec_ros/shell/roscore.sh"), argv[1], (void*)NULL);
    }

 
    pid_t carstate = fork();
    if(carstate == 0) {
        execl("/bin/sh", "sh", strcat(argv[1],"/autoexec_ros/shell/carstate.sh"), argv[1], (void*)NULL);
    }

    pid_t publish_gps = fork();
    if(publish_gps == 0) {
        execl("/bin/sh", "sh",  strcat(argv[1],"/autoexec_ros/shell/publish_gps.sh"), argv[1] ,(void*)NULL);
    }


    pid_t driver_main = fork();
    if(driver_main == 0) {
        execl("/bin/sh", "sh",  strcat(argv[1],"/autoexec_ros/shell/driver_main.sh"), argv[1], (void*)NULL);
    }

    pid_t ui = fork();
    if(ui == 0) {
        execl("/bin/sh", "sh",  strcat(argv[1],"/autoexec_ros/shell/ui.sh"),argv[1], (void*)NULL);
    }

    
    return 0;
}

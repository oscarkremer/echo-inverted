
#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <stdlib.h>


int main(int argc, char **argv)
{
        int fd;
        int active_tag, trigger_count, counterd, counter1, counter2, counter3, counterc, countercd, reset_counter, num_pulses;
        void *cfg;
        char *name= "/dev/mem";
        const int  freq = 1249988750;
        if (argc == 11) {
                active_tag = atof(argv[1]);
		        trigger_count = atof(argv[2]);
                counterd = atof(argv[3]);
                counter1 = atof(argv[4]);
                counter2 = atof(argv[5]);
                counter3 = atof(argv[6]);
                counterc = atof(argv[7]);
                countercd = atof(argv[8]);
                reset_counter = atof(argv[9]);
                num_pulses = atof(argv[10]);
                
        }
        else {
            active_tag = 0;
    		trigger_count = 0;
            counterd = 0;
            counter1 = 0;
	    	counter2 = 0;
            counter3 = 0;
		    counterd = 0;
            countercd = 0;
            reset_counter = 0;
            num_pulses = 0;
        }
        if ((fd = open(name, O_RDWR)) < 0) {
                perror("open");
                return 1;
        }
        cfg = mmap(NULL, sysconf(_SC_PAGESIZE), PROT_READ|PROT_WRITE, MAP_SHARED, fd, 0x40000000);
        *((uint32_t *)(cfg + 0)) = active_tag;
        *((uint32_t *)(cfg + 4)) = trigger_count;
        *((uint32_t *)(cfg + 8)) = counterd;
        *((uint32_t *)(cfg + 12)) = counter1;
        *((uint32_t *)(cfg + 16)) = counter2;
        *((uint32_t *)(cfg + 20)) = counter3;
        *((uint32_t *)(cfg + 24)) = counterc;;
        *((uint32_t *)(cfg + 28)) = countercd;
        *((uint32_t *)(cfg + 32)) = reset_counter;
        *((uint32_t *)(cfg + 36)) = num_pulses;
        
}
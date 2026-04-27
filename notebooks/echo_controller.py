import paramiko
from paramiko import SSHClient

class EchoController:
    def __init__(self, red_pitaya, username="root", password="root"):
        self.red_pitaya = red_pitaya
        self.username = username
        self.password = password
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.red_pitaya, username=self.username, password=self.password)
        self.enable = 0
        self.trigger_count = 0
        self.counter_delay = 0
        self.counter_stage1 = 0
        self.counter_stage2 = 0
        self.counter_stage3 = 0
        self.counter_control = 0
        self.counter_control_delay = 0

    def execute_command(self, command='/opt/echo_dinter/register', verbose= False):
        stdin, stdout, stderr = self.client.exec_command(' {} {} {} {} {} {} {} {} {}'.format(
            command, 
            self.enable,
            self.trigger_count, 
            self.counter_delay, 
            self.counter_stage1, 
            self.counter_stage2, 
            self.counter_stage3, 
            self.counter_control, 
            self.counter_control_delay))
        if verbose:
            print(stdout.readlines()) 
        
    def turn_off(self, verbose=False):
        self.enable = 0
        self.execute_command(verbose=verbose)

    def turn_on_pulses(self, frequency=0.1, reference_freq=50, verbose=False):
        self.enable = 1
        self.trigger_count = int(reference_freq/frequency)
        self.execute_command(verbose=verbose)

    def set_pulse_sequence(self, delay_time, time_stage_1, time_stage_2, time_stage_3, reference_time=8e-9, verbose=False):
        self.counter_delay = int(delay_time / reference_time)
        self.counter_stage1 = int(time_stage_1 / reference_time)
        self.counter_stage2 = int(time_stage_2 / reference_time)
        self.counter_stage3 = int(time_stage_3 / reference_time)
        self.execute_command(verbose=verbose)

    def set_control_sequence(self, delay_control, control_off_time, reference_time=8e-9, verbose=False):
        self.counter_control = int(control_off_time / reference_time)
        self.counter_control_delay = int(delay_control / reference_time)
        self.execute_command(verbose=verbose)
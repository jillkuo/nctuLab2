#!/usr/bin/python 

#the first line is necessary to run this code as a standalone executable

#This code is written by EECS 0610025 JILL KUO

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel 
from mininet.cli import CLI

class StructureOfTopo2(Topo):
	def build(self, n = 10):
		#add the Switches
		switch1 = self.addSwitch('s1')
		switch2 = self.addSwitch('s2')
		switch3 = self.addSwitch('s3')
		switch4 = self.addSwitch('s4')
		switch5 = self.addSwitch('s5')
		#add the Hosts
		host1 = self.addHost('h1')
		host2 = self.addHost('h2')
		host3 = self.addHost('h3')
		host4 = self.addHost('h4')
		host5 = self.addHost('h5')
		host6 = self.addHost('h6')
		host7 = self.addHost('h7')
		host8 = self.addHost('h8')
		host9 = self.addHost('h9')
		host10 = self.addHost('h10')
		#add the Links and set the property
		self.addLink(
                host9, 
                switch4, 
                bw = 30, 
                delay = '7ms', 
                loss = 12)
		self.addLink(
                switch4, 
                switch1, 
                bw = 38, 
                delay = '0.076ms', 
                loss = 4)
		self.addLink(
                switch3, 
                switch1, 
                bw = 35, 
                delay = '0.048ms', 
                loss = 2)
		self.addLink(
                host7, 
                switch1, 
                bw = 18, 
                delay = '4ms', 
                loss = 6)
		self.addLink(
                host3, 
                switch3, 
                bw = 15, 
                delay = '3ms', 
                loss = 8)
		self.addLink(
                host4, 
                switch3, 
                bw = 11, 
                delay = '2ms', 
                loss = 9)
		self.addLink(
                host8, 
                switch1, 
                bw = 20, 
                delay = '2ms', 
                loss = 8)
		self.addLink(
                switch5, 
                switch1, 
                bw = 40, 
                delay = '0.052ms', 
                loss = 2)
		self.addLink(
                host10, 
                switch5, 
                bw = 25, 
                delay = '5ms', 
                loss = 1)
		self.addLink(
                host6, 
                switch1, 
                bw = 25, 
                delay = '1ms', 
                loss = 7)
		self.addLink(
                host2, 
                switch2, 
                bw = 12, 
                delay = '4ms', 
                loss = 15)
		self.addLink(
                host1, 
                switch2, 
                bw = 14, 
                delay = '5ms', 
                loss = 13)
		self.addLink(
                host5, 
                switch1, 
                bw = 22, 
                delay = '3ms', 
                loss = 9)
		self.addLink(
                switch2, 
                switch1, 
                bw = 30, 
                delay = '0.087ms', 
                loss = 3)

def run_the_topo2():
	#create
	topo = StructureOfTopo2(n = 10)
	#set the type of topo, controller ,and link
	net = Mininet(
        topo = topo, 
        controller = OVSController,
        link = TCLink)
	#start the net
	net.start()
	#net.pingAll()
	#dump every hosts' and switches' connection
	dumpNodeConnections(net.hosts)
	dumpNodeConnections(net.switches)
	#enter in Mininet CLI mode
	CLI(net)

if __name__ == '__main__':
	setLogLevel('info')
	run_the_topo2()

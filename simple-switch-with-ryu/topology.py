from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

def create_topology():
  net = Mininet(controller=RemoteController, link=TCLink)

  info('*** Adding controller\n')
  net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)

  info('*** Adding hosts\n')
  h1 = net.addHost('h1', ip='10.0.0.1' )
  h2 = net.addHost('h2', ip='10.0.0.2' )
  h3 = net.addHost('h3', ip='10.0.0.3' )

  info('*** Adding switch\n')
  s1 = net.addSwitch('s1' )
  s2 = net.addSwitch('s2' )

  info('*** Creating links\n')
  net.addLink(h1, s1)#, intfName1='h1-eth0', intfName2='eth1')
  net.addLink(s1, s2)#, intfName1='eth0', intfName2='eth0')
  net.addLink(h2, s2)#, intfName1='eth0', intfName2='eth1')
  net.addLink(h3, s2)#, intfName1='eth0', intfName2='eth2')
  

  info('*** Starting network\n')
  net.start()

  info('*** Running CLI\n')
  CLI(net)

  info('*** Stopping network\n')
  net.stop()

if __name__ == '__main__':
  setLogLevel('info')
  create_topology()
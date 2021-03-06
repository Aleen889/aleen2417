“””Custom topology example
Two directly connected switches plus a host for each switch:
host --- switch --- switch --- host
h1 <–> s3 <–> s4 <–> h2
Adding the ‘topos’ dict with a key/value pair to generate our newly
defined
topology enables one to pass in ‘--topo=mytopo’ from the command line.
“””
from mininet.topo import Topo
class MyTopo( Topo ):
    def __init__( self ):
        “Create custom topo.”
        # Initialize topology
      Topo.__init__( self )
       # Add hosts and switches
      leftHost = self.addHost( ‘h1’ )
      rightHost = self.addHost( ‘h2’ )
      leftSwitch = self.addSwitch( ‘s3’ )
      rightSwitch = self.addSwitch( ‘s4’ )
    # Add links
      self.addLink( leftHost, leftSwitch )
      self.addLink( leftSwitch, rightSwitch )
      self.addLink( rightSwitch, rightHost )
topos = { ‘mytopo’: ( lambda: MyTopo() ) }
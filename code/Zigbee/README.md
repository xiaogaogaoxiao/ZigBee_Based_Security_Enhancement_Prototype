# ZigBee_Based_Security_Enhancement_Prototype
Railway transportation industry in North America actively uses the Advanced Train Control System (ATCS) protocol to remotely control train traffic signals. However, the ATCS protocol was designed in the early 80s, without consideration of cyber security and privacy of transmission. The wireless link in the ATCS network conveying the end-to-end packet delivery is designed on narrowband broadcasting transmission upon UHF. Protocol details of ATCS are open to public for vendor interoperability, and there is no encryption or dynamic design at any layer of the network. Several bits in the packet contain commands or status information corresponding to the railway traffic actions (e.g. traffic signals) that initialized by or transmitted to train dispatcher. Radio enthusiasts are able to develop homemade hardware and software to eavesdrop the ATCS network. By observing the physical railway traffic actions compared with the captured packets, the implications of the bits are hence decoded.  Although the eavesdropping actions are mostly passive, and the developers are benevolent enough that promised not to enable the program with encoding functions, it is still easy for some others to encode customized packets to maliciously attack the system via radio [1]. This brought up our motivation to design a prototype to improve the security of this radio link using some cost-effective network approaches.  
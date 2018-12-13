import random
import time
import matplotlib.pyplot as plt

class congestion_contorl:
    # we defined a random number: isRecd from (0, 5). Every time when isRecd equal with 0, that means the last TCP
    # package was not received. and when 0 was generated three times in succession, fast transmission happens.
    def __init__(self):
        self.MSS = 10
        self.RWND = 90
        self.SEND_DELAY = 0.01 + 0.01 * (100 - self.RWND)
        self.x = []
        self.y = []

    def run_with_fastRec(self):
        self.CWND = self.MSS
        self.SAMPLE_RTT = 1
        self.ACK_RECEIVE_COUNT = 0
        self.BANDWIDTH = 0
        self.DUP_COUNT = 0
        self.SSTHRESH = 40 * self.MSS
        self.DUP_ACK = 0
        self.ACK = 0
        self.x = []
        self.y = []
        plt.cla()
        n = 0
        while n < 100:
            self.ACK += 1
            time.sleep(0.05)
            isRecd = random.randint(0, 10)

            if isRecd != 0:
                n += 1
                self.x.append(n)
                print("Client : Num(%d) TCP package was sent, RWND(%d) Receive" % (self.ACK, self.RWND))
                self.ACK_RECEIVE_COUNT += 1

                if self.SSTHRESH == 0:
                    self.CWND *= 2
                    self.BANDWIDTH = self.CWND / self.SAMPLE_RTT
                    print("Client : CWND become %d, Exponential Increase Bandwidth(%3.1f)," % (self.CWND, self.BANDWIDTH))
                elif self.SSTHRESH > self.CWND:
                    self.CWND *= 2
                    self.BANDWIDTH = self.CWND / self.SAMPLE_RTT
                    print("Client : CWND become %d, Exponential Increase Bandwidth(%3.1f)," % (self.CWND, self.BANDWIDTH))
                elif self.SSTHRESH <= self.CWND:
                    self.CWND += self.MSS
                    self.BANDWIDTH = self.CWND / self.SAMPLE_RTT
                    print("Client : CWND become %d, Exponential Increase Bandwidth(%3.1f)," % (self.CWND, self.BANDWIDTH))
                self.y.append(self.CWND)


            else:
                print("Client : Num(%d) TCP package was sent, But RWND(%d) lost it" % (self.ACK, self.RWND))

            if (self.ACK - n) == 3:
                self.ACK -= 3
                print("Resent Num(%d) TCP package was sent, RWND(%d) lost" % (n, self.RWND))

                try:
                    self.DUP_ACK = 0
                    self.DUP_COUNT += 1

                    self.SSTHRESH = self.CWND / 2
                    self.CWND = self.SSTHRESH + 3 * self.MSS
                    self.BANDWIDTH = self.CWND

                    print("Client : Duplicated ACK - resend %d SEQ" % n)
                    print("Client : CWND become %d, Exponential Increase Bandwidth(%3.1f)," % (
                        self.CWND, self.BANDWIDTH))

                except:
                    continue
        plt.xlabel('ACK numbers')
        plt.ylabel('CWND')
        plt.title('Congestion Control with Fast Recovery')
        plt.plot(self.x, self.y, 'bo--')
        plt.show()

    def run_without_fastRec(self):
        self.CWND = self.MSS
        self.SAMPLE_RTT = 1
        self.ACK_RECEIVE_COUNT = 0
        self.BANDWIDTH = 0
        self.DUP_COUNT = 0
        self.SSTHRESH = 40 * self.MSS
        self.DUP_ACK = 0
        self.ACK = 0
        self.x = []
        self.y = []
        plt.cla()
        n = 0
        while n < 50:
            self.ACK += 1
            time.sleep(0.05)
            isRecd = random.randint(0, 5)

            if isRecd != 0:
                n += 1
                self.x.append(n)
                print("Client : Num(%d) TCP package was sent, RWND(%d) Receive" % (self.ACK, self.RWND))
                self.ACK_RECEIVE_COUNT += 1

                if self.SSTHRESH == 0:
                    self.CWND *= 2
                    self.BANDWIDTH = self.CWND / self.SAMPLE_RTT
                    print("Client : CWND become %d, Exponential Increase Bandwidth(%3.1f)," % (self.CWND, self.BANDWIDTH))
                elif self.SSTHRESH > self.CWND:
                    self.CWND *= 2
                    self.BANDWIDTH = self.CWND / self.SAMPLE_RTT
                    print("Client : CWND become %d, Exponential Increase Bandwidth(%3.1f)," % (self.CWND, self.BANDWIDTH))
                elif self.SSTHRESH <= self.CWND:
                    self.CWND += self.MSS
                    self.BANDWIDTH = self.CWND / self.SAMPLE_RTT
                    print("Client : CWND become %d, Exponential Increase Bandwidth(%3.1f)," % (self.CWND, self.BANDWIDTH))
                self.y.append(self.CWND)


            else:
                print("Client : Num(%d) TCP package was sent, But RWND(%d) lost it" % (self.ACK, self.RWND))

            if (self.ACK - n) == 3:
                self.ACK -= 3
                print("Resent Num(%d) TCP package was sent, RWND(%d) lost" % (n, self.RWND))

                try:
                    self.DUP_ACK = 0
                    self.DUP_COUNT += 1

                    self.SSTHRESH = self.CWND / 2
                    self.CWND = self.MSS
                    self.BANDWIDTH = self.CWND

                    print("Client : Duplicated ACK - resend %d SEQ" % n)
                    print("Client : CWND become %d, Exponential Increase Bandwidth(%3.1f)," % (
                        self.CWND, self.BANDWIDTH))

                except:
                    continue
        plt.xlabel('ACK numbers')
        plt.ylabel('CWND')
        plt.title('Congestion Control without Fast Recovery')
        plt.plot(self.x, self.y, 'ro--')
        plt.show()

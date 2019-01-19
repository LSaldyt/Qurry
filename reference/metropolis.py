# MH sampler for the correlation model described in the Cognition cheat sheet titled "Metropolis-Hastings sampling."
# Written by Ilker Yildirim, September 2012.

from scipy.stats import uniform, gamma, poisson
import matplotlib.pyplot as plt
import numpy
from numpy import log,exp,pi
from numpy.random import multinomial, multivariate_normal

# fix the random seed for replicability.
numpy.random.seed(12345678)

# Generate data
N=1000
data=multivariate_normal([0,0],[[1, 0.4],[0.4, 1]],N)
x=data[:,0]
y=data[:,1]


# make one big subplots and put everything in it.
f, (ax1,ax2,ax3)=plt.subplots(3,1)
# Plot the data
ax1.scatter(x,y,s=20,c='b',marker='o')

# Gibbs sampler
E=10000
BURN_IN=10

# Initialize the chain.
rho=0 # as if there's no correlation at all.

# Store the samples
chain_rho=numpy.array([0.]*(E-BURN_IN))

accepted_number=0.
for e in range(E):
    print("At iteration "+str(e))
    # Draw a value from the proposal distribution, Uniform(rho-0.07,rho+0.07); Equation 7
    rho_candidate=uniform.rvs(rho-0.07,2*0.07)

    # Compute the acceptance probability, Equation 8 and Equation 6.
    # We will do both equations in log domain here to avoid underflow.
    calc_accept_prob = lambda r : -3./2*log(1.-r**2) - N*log((1.-r**2)**(1./2)) - sum(1./(2.*(1.-r**2))*(x**2-2.*r*x*y+y**2))
    accept = calc_accept_prob(rho_candidate)
    accept = accept - calc_accept_prob(rho)
    accept=min([0,accept])
    accept=exp(accept)

    # Accept rho_candidate with probability accept.
    if uniform.rvs(0,1) < accept:
        rho=rho_candidate
        accepted_number=accepted_number+1
    else:
        rho=rho

    # store
    if e >= BURN_IN:
        chain_rho[e-BURN_IN]=rho

print("...Summary...")
print("Acceptance ratio is "+str(accepted_number/(E)))
print("Mean rho is "+str(chain_rho.mean()))
print("Std for rho is "+str(chain_rho.std()))
print("Compare with numpy.cov function: "+str(numpy.cov(data.T)))

# plot things
ax2.plot(chain_rho,'b')
ax2.set_ylabel('$rho$')
ax3.hist(chain_rho,50)
ax3.set_xlabel('$rho$')

plt.show()



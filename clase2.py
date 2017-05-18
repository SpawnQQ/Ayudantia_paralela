from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
root=0
l1=[]
l=[]
n=6/size
suma=0
sumatoria=0
if rank==root:
	l=[1,2,3,4,5,6]
l1=comm.bcast(l,root=root)

for p in range(n*rank,n*(rank+1)):
	suma=suma+l1[p]
print suma

suma=comm.gather(suma, root=root)  

print rank," ", l1, " ", suma

if rank==root:
	for i in range(size):
		sumatoria=sumatoria+suma[i]
	print sumatoria

#rank=0, 3*0-3*(0+1), 0-3
#rank=1, 3*1-3*(1+1), 3-6
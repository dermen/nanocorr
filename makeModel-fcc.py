from sys import argv
import numpy as np

#a           =  4.090 #silver lattice parameter

a           =  4.0786 # the real lattice parameter for gold!!
atomID      =  79
atom0       = np.array( [  0.,    0.,    0.] )
atom1       = np.array( [  0.,  a/2.,  a/2.] )
atom2       = np.array( [a/2.,    0.,  a/2.] )
atom3       = np.array( [a/2.,  a/2.,    0.] )
atoms       = np.vstack(  ( atom0, atom1, atom2, atom3 )  )
atom_per_unit   = atoms.shape[0]

#size_in_nm  = float ( input("size in nm: " ) ) 

size_in_nm  = float ( argv[1] ) 
size_in_ang = size_in_nm * 10.

center      = ( size_in_ang / 2., size_in_ang / 2., size_in_ang / 2. )

out_file_name = 'fcc_sphere_'+ str( size_in_nm) + 'nm.coor'
out_file = open( out_file_name,'w')

u1 = 0
while u1 < size_in_ang:
    u2 = 0
    while u2 < size_in_ang:
        u3 = 0
        while u3 < size_in_ang:
            i = 0
            while i < atom_per_unit:
                atomX = u1 + atoms[i][0]
                atomY = u2 + atoms[i][1]
                atomZ = u3 + atoms[i][2]
                radius = np.sqrt( ( atomX - center[0] )**2 + \
                                  ( atomY - center[1] )**2 + \
                                  ( atomZ - center[2] )**2  ) 
                if radius <= size_in_ang / 2:
                    #coors =  " ".join(  [str(atomX), str(atomY), str(atomZ), str(atomID) ] )
                    print >> out_file , atomX,atomY,atomZ,atomID
                    #np.savetxt( out_file, modelSphere, \
                     #       delimiter= " ", fmt='%.3f'  )
                i += 1
            u3 += a
        u2 += a
    u1 += a

out_file.close()

print "wrote file", 'fcc_sphere_'+ str( size_in_nm) + 'nm.coor' ,"."


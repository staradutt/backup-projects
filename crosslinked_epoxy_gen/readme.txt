Steps to make crosslinked epoxy:
1.  Create a box filled with individual molecules using EMC
2.  Once the lammps input file is generated, 
    write a python script to edit the input file genrated by EMC.
    The script should mark the atoms that are going to react in new atom types.(exl script included)
3.  Use lammps fix/bond-create(it will require as argument the atom types you created in step 2,
    to identify the atoms that it will create a bond between) with fix npt/nvt. 
    Read file named usedata.in to get an idea of how you go about doing this.
    Read point 4,5,6,7 before doing this step 
4.  You will also need to specify the bond energy coefficients. Read bonds class2 style to get 
    an idea about the coefficients you need to define the bond energy.
5.  Get the coefficients of the bond of the bond that you plan to create.
6.  Run step 3, with very low bond coefficients as arguments to fix/bond/create command.
    Otherwise if you use actual coefficients a lot of energy will be released on bond formation 
    and that will destabilise the simulation.
7.  Once the crosslinks are formed, manually change the bond coefficient to their original value and Run
    the simulations again. 
8.  Get the systems to required temperature and pressure.
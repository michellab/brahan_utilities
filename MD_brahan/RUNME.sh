gmx grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -o MD.tpr
gmx mdrun -deffnm MD -plumed plumed.dat

# Radiolysis of Liquid Methane in the TS1 Moderators


### This was the project which I completed whilst on a placement year as a part of the Neutronics Group at the ISIS Neutron and Muon source in 2020/21.

It was found that during operation, the TS1 liquid methane moderator was deteriorating due to a build up of a tar-like polymer as well as the presence of gaseous hydrogen. The build up of these defects was due to radiolysis of the liquid methane which resulted in chain reactions and subsequently the creation of the polymer mixture.

My task was to model the build up of the polymer and hydrogen in order to give a better understanding of the lifetime of the liquid methane moderator.
The basis of this work was an expansion of the model from a paper by David Evans. The paper used estimated data to calculate a approximate values for the hydrogen gas and polymer production rate. 
Using Evans' work I wrote the file 'Polymer_base_code.txt' which I was then able to refine using accurate values.

In order to model the build up of the defects more accurately, the data was obtained from an MCNP simulation ran by my manager. 
In the case of 'TS1_Current_Moderator_Final_Split.ipynb' the simulation was 800MeV protons onto the TS1 target where all subsequent neutrons, photons, helions etc were tracked. This gave the data present in 'Data_for_OT'.
As seen in the data as well as 'TS1_Current_Moderator_Final_Split.ipynb'', the moderator was split into a grid consisting of 48 sections. This allowed me to calculate the production rates of polymer and hydrogen per section as well as later implement the 'dwell_times_estimates.txt' data in order to give the overall production per section and as a whole for one cycle.  

## In This Repository:
- 'Polymer_base_code.txt' - The maths from the Evans paper. The first step to the project as the later funtions were based upon this. 
- 'Polymer_Production_Functions.py' - Once I understood the maths I wrote a python script containing all the functions I would use in the models.
- 'TS1_Current_Moderator_First_Split.ipynb' - This is the first run of my model. The moderator was split into 6 sections.
- 'TS1_Current_Moderator_Final_Split.ipynb' - The results came from the final run of the model using the data from the MCNP simulation in 'Data_for_OT' where the moderator was split into 48 sections and dwell times were applied. 


**Evans, D. 1995.** Irradiation effects in liquid methane used as a neutron moderator. Cryogenics, 35(11), pp.763-766.

#!/usr/bin/env python
# coding: utf-8

# # Polymer buildup and Hydrogen production in the ISIS Moderator

# The majority of the maths for this base code was taken from a paper by David Evans discussing the radiation damage effects in the liquid methane in the ISIS moderator and the radiation chemistry that accompanies it. 
# As quoted in his paper "It would seem most probable that the atomic hydrogen produced from the irradiation of methane, will react (by hydrogen abstraction) to produce molecular hydrogen and a di-radical:" "the polymer that is formed in thr moderator circuit, following bombardment withneutrons, results from a dimerization reaction of the methylene di-radical (*C*H2)"
# These mechanisms outlined are what likely causes the polymer 'sludge' to build up in the moderator. The following code outlines the maths for the three key areas:
# - Radicals per dose rate
# - Volume of Hydrogen production
# - Rate of polymer production
# 
# Evans, D., 1995. Irradiation effects in liquid methane used as a neutron moderator. Cryogenics, 35(11), pp.763-766.

# ### Radicals per Dose
# * G value in Mol/J

# \begin{aligned}
# moles/MGy = \frac {G_{mol/J}}{1000} \times 1e6 \\ \\ 
# radicals/MGy = moles \times 6.023e23
# \end{aligned}

# In[45]:


def moles_per_MGy(G_value):
    
    moles_per_g = G_value/1000    #since 1Gy = 1J/kg
    moles_per_MGy = moles_per_g * 1e6 
    
    return(moles_per_MGy)


# In[46]:


def radicals_per_dose(moles):
    
    rads_per_dose = moles * 6.023e23
    
    return(rads_per_dose)


# In[47]:


moles = moles_per_MGy(0.66e-6)

print (moles, 'mol/g')
print (radicals_per_dose(moles), 'radicals/g.MGy')


# ### Volume of Hydrogen gas produced

# #### Evans paper method
# - vols in cm3
# - dose in MGy/s

# \begin{aligned} 
# Vol_{STP} = mol \times 2.24e4 \\ \\
# Vol_H = Vol_{STP} \times \ Vol_{CH4} \times SG \times D
# \end{aligned}

# In[48]:


def vol_of_H_a (moles, CH4_vol, dose, SG):
    
    STP_vol = moles * 2.24e4
    
    h_produced = STP_vol * CH4_vol * SG * dose
    
    return(h_produced)


# In[49]:


print(vol_of_H_a(moles, 400, 0.01, 0.43), 'cm3/s')


# #### This is a different method from the University of Missouri paper
# * g-value in the paper is a primary g value so the value at the inital spur not the whole reaction (i think) - due to this i didnt use the g-value used in the paper i converted the g value from the one used in the Evans paper which i believe gives the Hydrogen production across the whole reaction not just the initial spur.
# * G value is worked out by converting mol/J to molecules/MeV
# * Dose is in MeV/s - also converted from MGy/s
# 
# Nrc.gov. 2021. Hydrogen Gas Generation Analysis. [online] Available at: <https://www.nrc.gov/docs/ML1535/ML15351A331.pdf> [Accessed 15 March 2021].

# \begin{aligned} 
# Mass_{CH4} = Vol_{CH4} \times \rho \\ \\
# G_{Molecules/MeV} = G_{mol/J} \times \frac {6.023e23}{6.242e12} \\ \\
# D_{MeV/s} = D_{MGy/s} \times Mass_{CH4} \times 6.242e18 \\ \\
# Vol_H = \frac {D_{MeV/s} \times G_{Molecules/MeV} \times 2.24e4}{6.023e23}
# \end{aligned}
# 

# In[50]:


def g_val_conversion(G_value):
    
    new_G_val = G_value * (6.023e23/6.242e12)
    
    return(new_G_val)
    


# In[51]:


new_g_val = g_val_conversion(0.66e-6)
print(new_g_val, 'molecules/MeV')


# In[52]:


def dose_rate_conversion(dose, mass_CH4):
    
    new_dose_rate = dose * mass_CH4 * 6.242e18
    
    return(new_dose_rate)


# In[53]:


new_dose_rate = dose_rate_conversion(0.01, 0.1696)
print(new_dose_rate, 'MeV/s')


# In[54]:


def vol_of_H_b(new_dose, new_g_value):
    
    h_production = (new_dose * new_g_value * 2.24e4)/ 6.023e23
    
    return(h_production)


# In[55]:


print(vol_of_H_b(new_dose_rate, new_g_val), 'cm3/s')


# ### Rate of polymer formation
# * assuming unit density
# * dose in MGy/s
# * mr is molecular weight
# * polymer (-CH2-)n - n value of polymer is difficult to quantify but thought to be no greater than 20 in the case of the methane moderator

# \begin{aligned}
# polymer/MGy = moles/MGy \times Mr \\ \\ 
# polymer/s = polymer/MGy \times D \times Mass_{CH4}
# \end{aligned}
# 

# In[56]:


def rate_of_pol_form(G_value, mr, dose, mass_CH4):
    
    polymer_form_per_dose = moles_per_MGy(G_value) * mr
    
    polymer_per_sec = polymer_form_per_dose * dose * mass_CH4
    
    return(polymer_per_sec)    


# In[57]:


print(rate_of_pol_form(0.22e-6, 300, 0.01, 169.6), 'g polymer/s')


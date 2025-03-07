# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 12:14:06 2025

@author: sala4
"""

import streamlit as st

def nectar_calculation(initial_pulp_mass, initial_brix, final_nectar_mass, final_brix):
    """
    Calculates the amount of water and sugar to add to a pulp to achieve a desired nectar concentration.
    
    Args:
        initial_pulp_mass (float): Initial mass of the pulp in kg.
        initial_brix (float): Initial Brix of the pulp.
        final_nectar_mass (float): Desired final mass of the nectar in kg.
        final_brix (float): Desired final Brix of the nectar.
    
    Returns:
        tuple: A tuple containing the amount of water and sugar to add in kg.
               Returns None if the calculations are not possible or if input is invalid
    """
    if not all(isinstance(arg, (int, float)) for arg in [initial_pulp_mass, initial_brix, final_nectar_mass, final_brix]):
        st.error("Error: Invalid input. All parameters must be numeric.")
        return None

    if initial_pulp_mass <= 0 or final_nectar_mass <= 0:
        st.error("Error: Input mass values must be positive.")
        return None

    if initial_brix < 0 or final_brix < 0:
        st.error("Error: Brix values must be non-negative.")
        return None

    try:
        initial_sugar = initial_pulp_mass * (initial_brix / 100)
        final_sugar = final_nectar_mass * (final_brix / 100)

        water_added = final_nectar_mass - initial_pulp_mass - (final_sugar - initial_sugar)
        sugar_added = final_sugar - initial_sugar

        if water_added < 0:
            st.error("Error: The calculation resulted in negative water addition. Check your input.")
            return None

        return water_added, sugar_added
    except Exception as e:
        st.error(f"An error occurred during calculations: {e}")
        return None

# Streamlit UI
st.title("Nectar Calculation")

# Input fields
initial_pulp_mass = st.number_input("Initial Pulp Mass (kg)", min_value=0.0, step=0.1, value=660.0)
initial_brix = st.number_input("Initial Brix (%)", min_value=0.0, step=0.1, value=7.0)
final_nectar_mass = st.number_input("Final Nectar Mass (kg)", min_value=0.0, step=0.1, value=800.0)
final_brix = st.number_input("Final Brix (%)", min_value=0.0, step=0.1, value=12.0)

# Button to trigger calculation
if st.button("Calculate"):
    result = nectar_calculation(initial_pulp_mass, initial_brix, final_nectar_mass, final_brix)
    
    if result is not None:
        water_added, sugar_added = result
        st.success(f"Amount of water to add: {water_added:.2f} kg")
        st.success(f"Amount of sugar to add: {sugar_added:.2f} kg")
import axios from 'axios';
import dotenv from 'dotenv';

export const apiClient = axios.create({
  baseURL: process.env.API_BASE_URL, 
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getPatients = async () => {
  try {
    const response = await apiClient.get('/patients/');
    return response.data;
  } catch (error) {
    console.error('Error fetching patients:', error);
    throw error;
  }
}

export const getDoctors = async () => {
  try {
    const response = await apiClient.get('/doctors/');
    return response.data;
  } catch (error) {
    console.error('Error fetching doctors:', error);
    throw error;
  }
}

export const getAppointments = async () => {
  try {
    const response = await apiClient.get('/appointments/');
    return response.data;
  } catch (error) {
    console.error('Error fetching appointments:', error);
    throw error;
  }
}
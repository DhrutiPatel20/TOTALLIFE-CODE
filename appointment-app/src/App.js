// src/App.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [appointments, setAppointments] = useState([]);
  const [filteredAppointments, setFilteredAppointments] = useState([]);
  const [timeRange, setTimeRange] = useState('');

  useEffect(() => {
    // Fetch appointments from the API (replace 'API_ENDPOINT' with your actual API endpoint)
    //('http://127.0.0.1:8000/api/appointments/')
    axios.get('http://127.0.0.1:8000/api/appointments/')
      .then(response => {
        setAppointments(response.data);
        console.log(response);
        setFilteredAppointments(response.data);
      })
      .catch(error => {
        console.error('Error fetching appointments:', error);
      });
  }, []);

  useEffect(() => {
    if (timeRange) {
      const filtered = appointments.filter(appointment => {
        // Assuming 'date_time:' is a property in the API response representing appointment time
        return appointment.date_time.includes(timeRange);
      });
      setFilteredAppointments(filtered);
    } else {
      setFilteredAppointments(appointments);
    }
  }, [appointments, timeRange]);

  return (
    <div className="container mx-auto mt-8">
      <h1 className="text-3xl font-bold mb-4">Appointments</h1>

      {/* Time Range Filter */}
      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700">Time Range:</label>
        <input
          type="text"
          value={timeRange}
          onChange={(e) => setTimeRange(e.target.value)}
          placeholder="Filter by time range"
          className="border p-2 rounded-md"
        />
      </div>

      {/* Appointment List */}
      <ul>
        {filteredAppointments.map(appointment => (
          <li key={appointment.id} className="mb-4">
            <strong>{appointment.patient}</strong>
            <p>{`Time: ${appointment.date_time} | clinician: ${appointment.clinician}`}</p>
          </li>
        ))}
      </ul>
    </div>
  )
};

export default App;


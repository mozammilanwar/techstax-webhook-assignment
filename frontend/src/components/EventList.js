import React, { useEffect, useState } from "react";
import axios from "axios";

function EventList() {
  const [events, setEvents] = useState([]);

  const fetchEvents = async () => {
    try {
      const res = await axios.get("http://localhost:5000/events"); 
      setEvents(res.data);
    } catch (err) {
      console.error("Error fetching events:", err);
    }
  };

  useEffect(() => {
    fetchEvents();
    const interval = setInterval(fetchEvents, 15000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Recent GitHub Events</h2>
      {events.map((event, index) => (
        <div key={index} style={{ borderBottom: "1px solid #ccc", marginBottom: "10px" }}>
          <p><strong>{event.author}</strong> performed <b>{event.actionType}</b></p>
          <p>From: {event.fromBranch} → To: {event.toBranch}</p>
          <p>{new Date(event.timestamp).toLocaleString()}</p>
        </div>
      ))}
    </div>
  );
}

export default EventList;

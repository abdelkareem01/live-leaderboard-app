"use client"

import { useEffect, useState } from "react";
import axios from 'axios';

export default function Home()
{
  const [users, setUsers] = useState([]);

  useEffect(() =>{
    const fetchUsers = async () =>
      {
        const result = await axios.get('http://127.0.0.1:8001/api/users/');
        setUsers(result.data);
      };
      
      fetchUsers();

      const interval = setInterval(fetchUsers, 3000);
      return () => clearInterval(interval);
  }, []);

  return (
  <div className="p-4">
    <h1 className="text-2xl font-bold mb-4"> Live Leaderboard</h1>
    <ul>
      {users.map(user => (
        <li key={user.id} className="bg-gray-100 p-2 rounded">
          {user.name} - {user.score}
        </li>
      ))}
    </ul>
  </div>
);
}
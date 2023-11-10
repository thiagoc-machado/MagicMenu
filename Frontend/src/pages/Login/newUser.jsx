import { useState } from "react";
import axios from "axios";

function NewUser() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    age: "",
    gender: "",
    address: "",
    city: "",
    state: "",
    zip: "",
    country: "",
    status: "",
    notes: "",
    photo: null,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // 1. Recupere o token JWT do Local Storage
    const token = localStorage.getItem('jwtToken');

    console.log("Token JWT enviado:", token);

    
    // 2. Configure o token JWT no cabeçalho da solicitação
    const headers = {
      Authorization: `Bearer ${token}`, // Use apropriadamente o esquema de autenticação (Bearer)
    };

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/users/",
        formData,
        { headers }
      );
      console.log("Usuário cadastrado com sucesso:", response.data);
      // Redirecionar ou realizar outras ações após o cadastro bem-sucedido
    } catch (error) {
      console.error("Erro ao cadastrar usuário:", error);
      // Lidar com erros
    }
  };

  return (
    <div>
      <h2>Cadastro de Usuário</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
          placeholder="Nome"
        />
        <input
          type="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
          placeholder=""
        />
        <input
          type="text"
          name="email"
          value={formData.email}
          onChange={handleChange}
          placeholder="E-mail"
        />
        <input
          type="text"
          name="phone"
          value={formData.phone}
          onChange={handleChange}
          placeholder="Telefone"
        />
        <input
          type="number"
          name="age"
          value={formData.age}
          onChange={handleChange}
          placeholder="Idade"
        />
        <input
          type="text"
          name="gender"
          value={formData.gender}
          onChange={handleChange}
          placeholder="Gênero"
        />
        <input
          type="text"
          name="address"
          value={formData.address}
          onChange={handleChange}
          placeholder="Endereço"
        />
        <input
          type="text"
          name="city"
          value={formData.city}
          onChange={handleChange}
          placeholder="Cidade"
        />
        <input
          type="text"
          name="state"
          value={formData.state}
          onChange={handleChange}
          placeholder="Estado"
        />
        <input
          type="text"
          name="zip"
          value={formData.zip}
          onChange={handleChange}
          placeholder="CEP"
        />
        <input
          type="text"
          name="country"
          value={formData.country}
          onChange={handleChange}
          placeholder="País"
        />
        <input
          type="text"
          name="status"
          value={formData.status}
          onChange={handleChange}
          placeholder="Status"
        />
        <input
          type="text"
          name="notes"
          value={formData.notes}
          onChange={handleChange}
          placeholder="Notas"
        />
        {/* Adicione um campo para upload de fotos, se necessário */}
        <button type="submit">Cadastrar Usuário</button>
      </form>
    </div>
  );
}

export default NewUser;

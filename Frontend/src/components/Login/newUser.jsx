function NewUser() {
    const [formData, setFormData] = useState({
      name: '',
      email: '',
      phone: null,
      age: null,
      gender: '',
      address: '',
      city: '',
      state: '',
      zip: null,
      country: '',
      status: '',
      notes: '',
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
  
      try {
        const response = await axios.post('/api/users/', formData);
        console.log('Usuário cadastrado com sucesso:', response.data);
        // Redirecionar ou realizar outras ações após o cadastro bem-sucedido
      } catch (error) {
        console.error('Erro ao cadastrar usuário:', error);
        // Lidar com erros, exibir mensagens de erro, etc.
      }
    };
  
    return (
      <div>
        <h2>Cadastro de Usuário</h2>
        <form onSubmit={handleSubmit}>
          {/* Renderize os campos do formulário com os respectivos nomes e valores do estado */}
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            placeholder="Nome"
          />
          {/* Repita o mesmo padrão para os outros campos do formulário */}
  
          <button type="submit">Cadastrar Usuário</button>
        </form>
      </div>
    );
  }
  
  export default NewUser;
  
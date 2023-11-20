import React from 'react';
import MenuItem from '../../components/menu_items/MenuItems';

const MenuItems = () => {
  const items = [
    {
      id: 1,
      nome: 'X-tudo',
      descricao: 'Tudo',
      valor: 15.99,
      imagemUrl: 'Hamburguer',
    },
    {
      id: 2,
      nome: 'Pizza',
      descricao: 'Peperone',
      valor: 19.99,
      imagemUrl: 'Pizza.jpg',
    },
    {
      id: 3,
      nome: 'Nome do Prato 3',
      descricao: 'Descrição do Prato 3',
      valor: 25.99,
      imagemUrl: 'Hotdog.jpg',
    }
  ];

  const filteredItems = items.filter(item => item.id > 0);

  return (
    <div>
      {filteredItems.map((item) => (
        <MenuItem key={'menu ' + item.id} id = {item.id} nome={item.nome} descricao={item.descricao} valor={item.valor} />
      ))}
    </div>
  );
};

export default MenuItems;

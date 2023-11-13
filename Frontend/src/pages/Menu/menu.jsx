import React from 'react';
import MenuItem from '../../components/menu_items/MenuItems';
import Hamburguer from '../../assets/hamburguer.jpg'
import '../../assets/hotdog.webp'
import '../../assets/batata.webp'

const MenuItems = () => {
  const items = [
    {
      id: 1,
      nome: 'X-tudo',
      descricao: 'Descrição do Prato 1',
      valor: 15.99,
      imagemUrl: 'Hamburguer',
    },
    {
      id: 2,
      nome: 'Nome do Prato 2',
      descricao: 'Descrição do Prato 2',
      valor: 19.99,
      imagemUrl: 'url_da_imagem_2.jpg',
    },
    {
      id: 3,
      nome: 'Nome do Prato 3',
      descricao: 'Descrição do Prato 3',
      valor: 25.99,
      imagemUrl: 'url_da_imagem_3.jpg',
    }
  ];

  return (
    <div>
      {items.map((item) => (
        <MenuItem key={'menu '+items.id} {...item} />
      ))}
    </div>
  );
};

export default MenuItems;

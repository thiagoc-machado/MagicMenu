import React from 'react';
import MenuItem from '../../components/menu_items/MenuItems';
import XTodoImage from '../../assets/X-tudo.jpg';
import PizzaImage from '../../assets/Pizza.jpg';
import HotdogImage from '../../assets/Hotdog.jpg';
import HamburguerImage from '../../assets/Hamburguer.webp';

const MenuItems = () => {
  const items = [
    {
      id: 1,
      nome: 'X-tudo',
      descricao: 'x-Tudo',
      valor: 15.99,
      imagemUrl: XTodoImage,
    },
    {
      id: 2,
      nome: 'Pizza',
      descricao: 'Peperone',
      valor: 19.99,
      imagemUrl: PizzaImage,
    },
    {
      id: 3,
      nome: 'Hotdog',
      descricao: 'Cachorro quente',
      valor: 25.99,
      imagemUrl: HotdogImage,
    },
    {
      id: 4,
      nome: 'Hamburguer',
      descricao: 'Hamburguer',
      valor: 15.99,
      imagemUrl: HamburguerImage,
    },
    {
      id: 5,
      nome: 'taco',
      descricao: 'taco',
      valor: 5.99,
      imagemUrl: XTodoImage,
    },
    {
      id: 6,
      nome: 'burger',
      descricao: 'burger',
      valor: 5.99,
      imagemUrl: XTodoImage,
    }
  ];

  const filteredItems = items.filter(item => item.id > 0);

  return (
    <div>
      {filteredItems.map((item) => (
        <MenuItem
          key={'menu ' + item.id}
          id={item.id}
          nome={item.nome}
          descricao={item.descricao}
          valor={item.valor}
          imagemUrl={item.imagemUrl}
        />
      ))}
    </div>
  );
};

export default MenuItems;

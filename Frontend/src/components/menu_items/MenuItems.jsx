import React from "react";
import "./MenuItems.css";

const MenuItem = ({ id, nome, descricao, valor, imagemUrl }) => {
  return (
    <div className="menu-item">
      <img src={imagemUrl} alt={nome} className="menu-item-img" />
      <div className="menu-item-details">
        <p className="menu-item-id">ID: {id}</p>
        <h3 className="menu-item-name">{nome}</h3>
        <p className="menu-item-description">{descricao}</p>
        <p className="menu-item-price">{`R$ ${valor.toFixed(2)}`}</p>
      </div>
    </div>
  );
};

export default MenuItem;

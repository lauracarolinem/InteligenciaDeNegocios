from crud.crud import *

if __name__ == "__main__":
  db = create_engine("sqlite:///base_pizzaria.db", echo=True)
  Session = sessionmaker(bind=db)
  Base = declarative_base()
  
  Base.metadata.create_all(db)

  criar_Pedido(nomeCliente='Laura' , valor=25.00, id_pizza=1)
  read_Pedido()
  update_Pedido()
  delete_Pedido()
  
  criar_cardapioPizzas(nomePizza="Calabresa", tamanho="Grande", preco=25.00, descricao='Pizza com molho, queijo e calabresa')
  read_cardapioPizzas()
  update_cardapioPizzas()
  delete_cardapioPizzas()

  criar_Mesa(numeroMesa=3, status=True, idPedido=1)
  read_Mesa()
  update_Mesa()
  delete_Mesa()
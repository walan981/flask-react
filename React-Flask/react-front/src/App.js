
import './App.css';
import React, {useState, useEffect} from 'react';

function App() {

  const [data, setData] = useState([{}])

  // const [comment, setComment] = useState('')
  // const[user, setUser] = useState('')

  const[text,setText] = useState('')
  const[username,setUsername] = useState('')


  //1 - Obter resposta do servidor via fetch
  //2 - passar a resposta como objeto javascript
  //3 - extrair dados da consulta

  useEffect(()=>{
    fetch("/api/post").then(
      res=>{
        return res.json() //retorna objeto JS em outra promisse
      })
      .then((data)=>{
        console.log(data);
        console.log(data.length)
        setData(data)
      }
    )
  },[]);

  console.log(data)


  //ADICIONAR COMENTARIO

  const sendComment = async(e) =>{
    e.preventDefault();
    // const comment2Send = comment;
    // setComment('');

    // AQUI VAI UM FETCH DE ADICIONAR COMENTARIO NA DATABASE

    let _data = {
      username: username,
      text: text,
    };
    console.log(_data)

    await fetch("/api/post/add",{
      method: 'POST',
      body: JSON.stringify(_data),
      headers: { "Content-type": "application/json; charset=UTF-8" },
    }).then((res)=>{
      console.log(res);

      if(res.ok === true){
        console.log('comentario adicionado')
      }else{
        console.log('Erro na criacao')
      }
    })
    
  }


  // EDITAR COMENTARIO

  const editComment = async(e) =>{
    e.preventDefault();
  }



  // DELETAR COMENTARIO

  const deleteComment = async(e) =>{
    e.preventDefault();
    var id  = e.target.parentNode.getAttribute('postId')
    console.log(id)

    await fetch(`/api/post/delete/${id}`,{
      method: 'DELETE',
    }).then((res)=>{
      console.log(res);

      if(res.ok === true){
        console.log('comentario Deletado')
      }else{
        console.log('Erro no delete')
      }
    })
    
  }



  return (

    <div className="App">
      <h1>Postagem</h1>

    {/* Renderiza lista de filmes */}
      {(typeof data == 'undefined')?(
        <p>Loading...</p>
      ):(
        <>
          {(data.length>=1)?(
          //(id, title, duration, released)
            data.map((item)=>(
              <div key={item} postId={item.id}>
                <p>
                  <b>{item.username}</b> : {item.text}
                </p>
                <button type='submit'
                onClick={e=>deleteComment(e)}>
                  Delete
                </button>
              </div>
              ))
            ):(
              <p>Lista Vazia</p>
            )}
          </>
        )
      }


      <div>
          <form>

          <input type='text'
              value={username}
              placeholder='usuario'
              onChange={e=>setUsername(e.target.value)}>
          </input>

            <input type='text'
              value={text}
              placeholder='comentar'
              onChange={e=>setText(e.target.value)}>
            </input>


            <button 
              type='submit'
              disabled={!text.trim()}
              onClick={sendComment}
              className='font-semibold text-blue-400'>
              Post
            </button>

          </form>
      </div>


    </div>
  );
}

export default App;

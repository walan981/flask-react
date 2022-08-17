
import './App.css';
import React, {useState, useEffect} from 'react';

function App() {

  const [data, setData] = useState([{}])
  const [comment, setComment] = useState('')
  const[user, setUser] = useState('')

  const[title, setTitle] = useState('')
  const[duration, setDuration] = useState(0)
  const[released, setReleased] = useState('')

 
  //1 - Obter resposta do servidor via fetch
  //2 - passar a resposta como objeto javascript
  //3 - extrair dados da consulta

  useEffect(()=>{
    fetch("/api/movies").then(
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
      title: title,
      duration: duration,
      released: released,
    };
    console.log(_data)

    await fetch("/api/movies/add",{
      method: 'POST',
      body: JSON.stringify(_data),
      headers: { "Content-type": "application/json; charset=UTF-8" },
    }).then((res)=>{
      console.log(res);

      if(res.ok === true){
        console.log('Filme adicionado')
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

    await fetch(`/api/movies/delete/${id}`,{
      method: 'DELETE',
    }).then((res)=>{
      console.log(res);

      if(res.ok === true){
        console.log('Filme Deletado')
      }else{
        console.log('Erro no delete')
      }
    })
    
  }





  


  return (

    <div className="App">
      <h1>Lista de Filmes</h1>

    {/* Renderiza lista de filmes */}
      {(typeof data == 'undefined')?(
        <p>Loading...</p>
      ):(
        <>
          {(data.length>1)?(
          //(id, title, duration, released)
            data.map((item)=>(
              <div key={item} postId={item.id}>
                <p>
                  {item.title}, {item.duration} minutos, {item.released} 
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

          {/* <input type='text'
              value={user}
              placeholder='usuario'
              onChange={e=>setUser(e.target.value)}>
          </input>

            <input type='text'
              value={comment}
              placeholder='comentar'
              onChange={e=>setComment(e.target.value)}>
            </input> */}


            <input type='text'
                value={title}
                placeholder='titulo'
                onChange={e=>setTitle(e.target.value)}>
            </input>

            <input type='number'
              value={duration}
              placeholder='duracao'
              onChange={e=>setDuration(e.target.value)}>
            </input>

            <input type='text'
              value={released}
              placeholder='estreia (YY-MM-DD)'
              onChange={e=>setReleased(e.target.value)}>
            </input>


            <button 
              type='submit'
              disabled={!title.trim()}
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

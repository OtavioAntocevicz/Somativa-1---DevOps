import {ChangeEvent, useState} from "react";

const Formulario = () => {
  const [email, setEmail] = useState<string>();
  const [password, setPassword] = useState<string>();
  const [isLogged, setIsLogged] = useState<boolean>(false);
  const [isLoginError, setIsLoginError] = useState<boolean>(false);

  const handleLogin = () => {
    if (email === "eduardo.lino@pucpr.br" && password === "123456") {
      setIsLogged(true);
      setIsLoginError(false);
    } else {
      setIsLogged(false);
      setIsLoginError(true);
    }
  };

  const onEmailInputChange = (event: ChangeEvent<HTMLInputElement>) => {
    setEmail(event.target.value);
  };

  const onPasswordInputChange = (event: ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };

  return (
    <div style={{display: "block"}}>
      <h2>Login</h2>
      <input type="email" placeholder="Email" onChange={onEmailInputChange} />
      <br />
      <input
        type="password"
        placeholder="Senha"
        onChange={onPasswordInputChange}
      />
      <br />
      <button type="submit" onClick={handleLogin}>
        Acessar
      </button>
      <br />
      {isLogged && <p>Acessado com sucesso!</p>}
      {isLoginError && <p>Usuário ou senha incorretos!</p>}
    </div>
  );
};

export default Formulario;

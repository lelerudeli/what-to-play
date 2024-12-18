import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Login, LoginResponse } from '../models/login.models';
import { Cadastro } from '../models/cadastro.model';
import { Jogo } from '../models/jogo.model';

@Injectable({
  providedIn: 'root'
})
export class PythonService {

  readonly API = 'http://127.0.0.1:5000';

  constructor(
    private http: HttpClient
  ) { }

  login(body: Login): Observable<any> {
    return this.http.post<any>(`${this.API}/login`, body);
  }

  storeUserData(user: LoginResponse): void {
    const { senhaUsuario, token, ...userWithoutSenha } = user;
    localStorage.setItem('user', JSON.stringify(userWithoutSenha));
    localStorage.setItem('token', token);
  }

  cadastroUsuario(body: Cadastro): Observable<any> {
    return this.http.post<any>(`${this.API}/cadastrar/usuario`, body);
  }

  getAllJogos(): Observable<any> {
    return this.http.get<any>(`${this.API}/jogos`);
  }

  cadastroJogo(body: Jogo): Observable<any> {
    return this.http.post<any>(`${this.API}/cadastrar/jogo`, body);
  }

  perfil(): Observable<any> {
    const token = localStorage.getItem('token');
    const headers = {
      Authorization: `Bearer ${token}`,
    };
  
    return this.http.get<any>(`${this.API}/perfil`, { headers });
  }
}

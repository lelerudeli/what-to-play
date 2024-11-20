import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class PythonService {

  readonly API = `http://127.0.0.1:5000`

  constructor(
    private http: HttpClient
  ) { }


  getdata() {
    return this.http.get(`${this.API}/`);
  }
}


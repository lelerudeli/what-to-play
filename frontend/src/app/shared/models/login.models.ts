export interface Login {
    email: string,
    senha: string
}

export interface LoginResponse extends Login {
    id: number,
    nome: string
}
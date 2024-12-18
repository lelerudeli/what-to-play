export interface Login {
    emailUsuario: string,
    senhaUsuario: string
}

export interface LoginResponse extends Login {
    id: number,
    nome: string,
    token: string
}
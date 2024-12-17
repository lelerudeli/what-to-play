export interface MinimumCards {
    tipo: TypeCardsEnum,
    nome: string,
    classificacao: ClassificacaoCards
}

export enum TypeCardsEnum {
    BARALHO = "BARALHO",
    CONVERSACAO = "CONVERSACAO",
    PAPELECANETA = "PAPELECANETA"
}

export enum ClassificacaoCards {
    DEZOITO = "18",
    DEZESSEIS = "16",
    CATORZE = "14",
    DOZE = "12",
    DEZ = "10",
    LIVRE = "LIVRE"
}


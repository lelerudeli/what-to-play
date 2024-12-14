export interface MinimumCards {
    tipo: TypeCardsEnum,
    nome: string,
    classificacao: ClassificacaoCards
}

export enum TypeCardsEnum {
    BARALHO = "BARALHO",
    CONVERSA = "CONVERSA",
    PAPEL = "PAPEL"
}

export enum ClassificacaoCards {
    DEZOITO = "DEZOITO",
    DEZESSEIS = "DEZESSEIS",
    CATORZE = "CATORZE",
    DOZE = "DOZE",
    DEZ = "DEZ",
    LIVRE = "LIVRE"
}


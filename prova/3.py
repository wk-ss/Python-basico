class Conta :
    def __init__ ( self, numero ):
        self.num = numero
        self.operacoes = [ ]
        self.__saldo = 0
        def debitar( self , valor , data ) :
            self.__saldo =self .__saldo - valor
            self .opercoes . append({ ' ti p o ' : 'D' , ' v al o r ' : valor , ' data ' : data } )
        def cretidar ( self , valor , data ) :
            self . __saldo = self . __saldo + valor
            self .opercoes . append ({ ' ti p o ' : 'C ' , ' v al o r ' : valor , ' data ' : data } )
        def saldoAtual ( self ) :
            return self . __saldo
class EspadaMarina(Espada):
	#esta clase ya contiene todos los metodos y propiedades de su clase padre Espada
	#ahora vamos a añadirle la nueva funcionalidad
	def ataqueTsunami(self, objetivo):
		
		#verificamos que el objetivo sea de tipo marino para poder restarle puntos de vida 
		if objetivo[‘tipo’] == ‘marino’:
			#restamos al objetivo 10 puntos de vida pero sumamos su resistencia
			objetivo['vida'] = objetivo['vida'] - 10 + objetivo['resistencia']
		else:
			#si el objetivo no es de tipo marino mostramos el siguiente mensaje
			print(‘este ataque solo funciona contra enemigos marinos!!’)

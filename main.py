import sys

from cubeMaker import Color, CubeMaker, GroundMaker
from panda3d.core import WindowProperties, Texture, TextureStage, TexGenAttrib
from panda3d.core import DirectionalLight, PointLight, AmbientLight, CardMaker
from direct.showbase.ShowBase import ShowBase

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # dlight = DirectionalLight('my dlight')
        # dlight.setColor((0.3, 0.3, 0.3, 1))
        # dlnp = self.render.attachNewNode(dlight)
        # dlnp.setPos(-20.0, -20.0, 10.0)
        # dlnp.setHpr(0.0, -20.0, 0.0)
        # self.render.setLight(dlnp)

        plight = PointLight('plight')
        plight.setColor((0.3, 0.3, 0.3, 1))
        plnp = self.render.attachNewNode(plight)
        plnp.setPos(-20.0, -20.0, 10.0)
        self.render.setLight(plnp)

        ambientLight = AmbientLight('ambientLight')
        ambientLight.setColor((0.6, 0.6, 0.6, 1))
        ambientLightNP = self.render.attachNewNode(ambientLight)
        self.render.setLight(ambientLightNP)

        self.setBackgroundColor(0.0, 0.0, 0.0)
        self.disableMouse()

        self.camera.setPos(0.0, 0.0, 30.0)
        self.camera.setHpr(-90.0, -90.0, 0.0)

        grass_tex = self.loader.loadTexture("./assets/field/field.png")
        print( grass_tex.getOrigFileXSize(), grass_tex.getOrigFileYSize() )
        grass_tex.setWrapU(Texture.WM_border_color)
        grass_tex.setWrapV(Texture.WM_border_color)
        grass_tex.setBorderColor((0.4, 0.5, 1, 1))

        # ts = TextureStage('ts')
        # ts.setMode(TextureStage.MDecal)
        ground = GroundMaker(color=Color.WHITE, size = 1).generate()
        ground.setTexGen(TextureStage.getDefault(), TexGenAttrib.MWorldCubeMap)
        ground.setTexScale(TextureStage.getDefault(), 8, 4)
        ground.setTexture( grass_tex )
        ground.setPos(0.0, 0.0, 0.0)
        ground.reparentTo(self.render)

        # myCardMaker = CardMaker("my card maker")

        # card = self.render.attachNewNode(myCardMaker.generate())
        # card.setP(-90) # This rotates the card to face upwards
        # card.setPos(0.0, 0.0, 0.1)
        # card.setScale(10, 10, 0)
        # card.setTexture( grass_tex )

        # cube = CubeMaker(color=Color.RED).generate()
        # cube.setPos(0.0, 0.0, 2.0)
        # cube.reparentTo(ground)

        # cube2 = CubeMaker(color=Color.RED).generate()
        # cube2.setPos(5.0, 0.0, 2.0)
        # cube2.reparentTo(ground)





game = Game()
game.accept("escape", sys.exit)
game.accept("a", game.render.analyze)
game.accept("o", game.oobe)
game.run()
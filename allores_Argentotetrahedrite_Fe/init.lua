allores_argentotetrahedrite_fe = {}
local S = minetest.get_translator(minetest.get_current_modname())

if minetest.get_modpath("allores_argentotetrahedrite_fe") ~= nil then
-------------------------------------------------
-- node --
minetest.register_node("allores_argentotetrahedrite_fe:Argentotetrahedrite_Fe", {
	description = S("Argentotetrahedrite_Fe") .. "\n" .. S("(All the minerals of the Earth, thanks to RRUFF for the list of minerals)"),
	tiles = {"allores.png"},
	groups = {cracky=3},
})

-------------------------------------------------
-- craft --
minetest.register_craft({
	type = "cooking",
	output = "allores_argentotetrahedrite_fe:allores2 1",
	recipe = "allores_argentotetrahedrite_fe:Argentotetrahedrite_Fe",
	cooktime = 1
})
-------------------------------------------------
--mapgen--

	minetest.register_ore({
		ore_type        = "scatter",
		ore             = "allores_argentotetrahedrite_fe:Argentotetrahedrite_Fe",
		wherein         = {"default:sand","default:sandstone","default:silver_sand","default:silver_sandstone","default:lava_source","default:lava_flowing","default:dirt_with_snow","default:snow","default:stone"},
		clust_scarcity  = 32 * 32 * 32,
		clust_size      = 5,
		y_max           = -10,
		y_min           = -31000,
		noise_threshold = 0.0,
		noise_params    = {
			offset = 0.5,
			scale = 0.2,
			spread = {x = 5, y = 5, z = 5},
			seed = -316,
			octaves = 1,
			persist = 0.0
		},
	})

end
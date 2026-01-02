-- filters/hide-solutions.lua
local function meta_bool(x, default)
  if x == nil then return default end
  if x.t == "MetaBool" then return x.c end
  if x.t == "MetaString" then return x.c == "true" end
  return default
end

function Div(el)
  local show = meta_bool(PANDOC_STATE.meta["show-solutions"], true)
  if el.classes:includes("solution") and not show then
    return {}  -- remove the whole block
  end
end
-----------------------------------------------------------
-- Keymaps configuration file: keymaps of neovim
--- and plugins.
-----------------------------------------------------------

local map = vim.api.nvim_set_keymap
local default_opts = {noremap = true, silent = true}

-----------------------------------------------------------
-- Neovim shortcuts:
-----------------------------------------------------------
-- basic autopair

--map('i', '"', '""<left>', default_opts)
--map("i", "'", "''<left>", default_opts)
--map('i', '`', '``<left>', default_opts)
--map('i', '(', '()<left>', default_opts)
---map('i', '[', '[]<left>', default_opts)
--map('i', '{', '{}<left>', default_opts)
--map('i', '{<CR>', '{<CR}<ESC>0', default_opts)
--map('i', '{;<CR>', '{<CR};<ESC>0', default_opts)

-- clear search highlighting
map('n', '<leader>c', ':nohl<CR>', default_opts)

-- map Esc to kk
map('i', 'kk', '<Esc>', {noremap = true})

-- don't use arrow keys
map('', '<up>', '<nop>', {noremap = true})
map('', '<down>', '<nop>', {noremap = true})
map('', '<left>', '<nop>', {noremap = true})
map('', '<right>', '<nop>', {noremap = true})

-- fast saving with <leader> and s
map('n', '<leader>s', ':w<CR>', default_opts)
map('i', '<leader>s', '<C-c>:w<CR>', default_opts)

-- move around splits using Ctrl + {h,j,k,l}
map('n', '<C-h>', '<C-w>h', default_opts)
map('n', '<C-j>', '<C-w>j', default_opts)
map('n', '<C-k>', '<C-w>k', default_opts)
map('n', '<C-l>', '<C-w>l', default_opts)

-- close all windows and exit from neovim
map('n', '<leader>q', ':qa<CR>', default_opts)

-- jump out of parenthesis
map('i', 'jj', '<C-o>A', {noremap = true})
--map('i', 's-j', '<esc>la', {noremap = true})



-- move left and right in insert mode
--map('i', '<s-h>', '<left>', default_opts)
--map('i', '<s-l>', '<right>', default_opts)

-----------------------------------------------------------
-- Plugins shortcuts:
-----------------------------------------------------------
-- Nvim-Tree
map('n', '<C-n>', ':NvimTreeToggle<CR>', default_opts)       -- open/close
map('n', '<leader>r', ':NvimTreeRefresh<CR>', default_opts)  -- refresh
map('n', '<leader>n', ':NvimTreeFindFile<CR>', default_opts) -- search file




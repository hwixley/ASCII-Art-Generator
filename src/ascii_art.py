import numpy as np
from args_parser import ArgsParser

class AsciiArt:

    def __init__(self):
        self.args = ArgsParser()

    def print_ascii_image(self):
        for row in self.get_ascii_image():
            print("".join(row))

    def get_ascii_image(self):
        img_arr = self.args.get_resized_bw_img()
        charset = self.args.get_charset()
        sampler = self.args.get_sampler()
        lower_ptg = self.args.get_lower_ptg()
        upper_ptg = self.args.get_upper_ptg()

        ptgs = self.get_ptgs(len(charset), sampler, lower_ptg, upper_ptg)
        return self.get_ascii_image_arr(img_arr, charset, ptgs)
    
    def get_ascii_image_arr(self, img_arr, charset, ptgs):
        ascii_arr = [[" " for _ in range(img_arr.shape[1])] for _ in range(img_arr.shape[0])]

        for i, ptg in enumerate(ptgs):
            last_ptg = ptgs[i-1] if i > 0 else 0
            lt_idxs = self.tuple_set(np.argwhere(img_arr < ptg * 255).tolist())
            gt_idxs = self.tuple_set(np.argwhere(img_arr >= last_ptg * 255).tolist())

            idxs = list(set(lt_idxs).intersection(gt_idxs))

            for idx in idxs:
                ascii_arr[idx[0]][idx[1]] = charset[i]*self.args.get_ascii_pixel_size()[1]

            if self.args.get_ascii_pixel_size()[0] > 1:
                for idx in idxs:
                    for j in range(self.args.get_ascii_pixel_size()[0]):
                        if idx[1]+j < len(ascii_arr[idx[0]]):
                            ascii_arr[idx[0]][idx[1]+j] = charset[i]*self.args.get_ascii_pixel_size()[1]
                        else:
                            ascii_arr[idx[0]] += charset[i]*self.args.get_ascii_pixel_size()[1]
        return ascii_arr

    def get_ptgs(self, n, sampler, lower_ptg, upper_ptg):
        if sampler == "linear":
            return [0] + np.linspace(lower_ptg, upper_ptg, n-2).tolist() + [1]
        elif sampler == "log":
            return np.logspace(lower_ptg, upper_ptg, n-1).tolist() + [1]
        elif sampler == "exp":
            return np.exp(np.linspace(lower_ptg, upper_ptg, n-1)).tolist() + [1]
        else:
            raise ValueError("Invalid sampler.")

    def tuple_set(self, seq):
        return {tuple(item) for item in seq}


if __name__ == "__main__":
    aa = AsciiArt()
    aa.print_ascii_image()